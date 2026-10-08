#!/usr/bin/env python3
"""Seri 2 video üretici: senaryo -> görüntü (HTML) + ses (edge-tts, Ahmet) -> kinocut ile video.

Kullanım:
    python uret.py md                  # SENARYOLAR.md dosyasını yazar
    python uret.py video 9             # videolar/09_*.mp4 ve .srt üretir
    python uret.py video 9 --kareler   # yalnızca kontrol kareleri

Gerekenler: kinocut (pip install kinocut), edge-tts, playwright (+ Chromium), ffmpeg.
Bu bulut ortamında: Chromium /opt/pw-browsers/chromium, ağ proxy'si için CA paketi kullanılır.
"""
import argparse
import asyncio
import html
import json
import os
import re
import subprocess
import sys
import tempfile
import wave
from pathlib import Path

KLASOR = Path(__file__).resolve().parent
KOK = KLASOR.parent
sys.path.insert(0, str(KLASOR))
from senaryolar import VIDEOLAR  # noqa: E402

KINOCUT = os.environ.get("KINOCUT", "kinocut")
SES = "tr-TR-AhmetNeural"
HIZ = "+0%"
PERDE = "+0Hz"
FPS = 5                      # görüntüler durağan; kinocut create-from-images her kareyi ayrı işlediği için düşük tutuldu
GEN, YUK = 1920, 1080
BAS, SON = 0.9, 1.8          # ilk cümleden önce, son cümleden sonra sessizlik (sn)
BOSLUK_ICERIDE, BOSLUK_SAHNE = 0.30, 0.80
ORNEK_HIZ = 44100

# --- ses okunuşu: İngilizce adlar Türkçe sesle doğru okunsun (altyazıda doğru yazılış kalır) ---
SOZLUK = [
    (r"GitGuardian", "Git Gardiyın"), (r"GitHub", "Git Hab"), (r"commit", "komit"),
    (r"Cursor", "Körsır"), (r"Shein", "Şiin"), (r"Google Play", "Gugıl Pley"), (r"Google", "Gugıl"),
    (r"ETBİS", "E Te Bi İs"), (r"İYS", "İ Ye Es"), (r"KVKK", "Ka Ve Ka Ka"), (r"GDPR", "Ge De Pe Er"),
    (r"Roblox", "Robloks"), (r"Veracode", "Verakod"), (r"Supabase", "Süpabeys"), (r"Lovable", "Lavıbıl"),
    (r"UpGuard", "Apgard"), (r"OWASP", "Ovasp"), (r"WCAG", "Ve Ce A Ge"), (r"EN 301 549", "E En üç yüz bir beş yüz kırk dokuz"),
    (r"API 36", "A Pe İ otuz altı"), (r"Android 16", "Android on altı"), (r"Apple", "Epıl"), (r"Steam", "Stim"),
    (r"Creator Docs", "Kriyeytır Doks"), (r"Luau", "Lu-au"), (r"Unity", "Yuniti"), (r"Unreal", "Anriıl"),
    (r"Godot", "Godo"), (r"Swift", "Svift"), (r"Kotlin", "Kotlin"), (r"Flutter", "Flatır"),
    (r"React Native", "Riyakt Neytiv"), (r"React", "Riyakt"), (r"Electron", "Elektron"), (r"Tauri", "Tavri"),
    (r"TypeScript", "Tayp Skript"), (r"JavaScript", "Cava Skript"), (r"HTML", "Ha Te Em El"), (r"CSS", "Ce Es Es"),
    (r"Python", "Paython"), (r"Vue", "Vyu"), (r"Svelte", "Svelt"), (r"Blueprint", "Blupırint"), (r"GDScript", "Ge Di Skript"),
    (r"Replit", "Replit"), (r"TANDEM", "Tandem"),
]

BIRLER = ["", "bir", "iki", "üç", "dört", "beş", "altı", "yedi", "sekiz", "dokuz"]
ONLAR = ["", "on", "yirmi", "otuz", "kırk", "elli", "altmış", "yetmiş", "seksen", "doksan"]


def _yuzluk(n):
    s = ""
    y, k = divmod(n, 100)
    if y:
        s += ("" if y == 1 else BIRLER[y] + " ") + "yüz "
    o, b = divmod(k, 10)
    s += ONLAR[o] + (" " if o and b else "") + BIRLER[b]
    return s.strip()


def tr_sayi(n):
    if n == 0:
        return "sıfır"
    parcalar = []
    for deger, ad in ((10**9, "milyar"), (10**6, "milyon"), (1000, "bin")):
        q, n = divmod(n, deger)
        if q:
            parcalar.append(("" if (ad == "bin" and q == 1) else _yuzluk(q) + " ") + ad)
    if n:
        parcalar.append(_yuzluk(n))
    return " ".join(p.strip() for p in parcalar)


def sese_cevir(metin):
    for kalip, yeni in SOZLUK:
        metin = re.sub(kalip, yeni, metin)
    metin = re.sub(r"\d{1,3}(?:\.\d{3})+|\d+", lambda m: tr_sayi(int(m.group(0).replace(".", ""))), metin)
    return metin


# --- yardımcılar ---
def calistir(komut, **kw):
    r = subprocess.run(komut, capture_output=True, text=True, **kw)
    if r.returncode != 0:
        raise RuntimeError(f"Komut başarısız: {' '.join(map(str, komut[:6]))}...\n{r.stdout[-800:]}\n{r.stderr[-1500:]}")
    return r.stdout


def sure(dosya):
    return float(calistir(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(dosya)]).strip())


def srt_zaman(t):
    t = max(t, 0)
    s, ms = divmod(int(round(t * 1000)), 1000)
    d, s = divmod(s, 60)
    h, d = divmod(d, 60)
    return f"{h:02d}:{d:02d}:{s:02d},{ms:03d}"


# --- görüntü (HTML) ---
CSS = """
*{box-sizing:border-box;margin:0;padding:0}
body{width:1920px;height:1080px;overflow:hidden;color:#eef1ff;background:#0b1020;
 font-family:'DejaVu Sans','Noto Sans',sans-serif;position:relative}
.glow{position:absolute;inset:0;background:radial-gradient(900px 600px at 82% 18%, var(--renk-soluk), transparent 70%),
 linear-gradient(135deg,#0b1020 0%,#141a33 100%)}
.ust{position:absolute;left:96px;top:48px;font-size:26px;color:#aab2d5;display:flex;align-items:center;gap:14px;letter-spacing:.5px}
.nokta{width:16px;height:16px;border-radius:4px;background:var(--renk)}
.no{position:absolute;right:96px;top:48px;font-size:26px;color:#aab2d5}
.ilerleme{position:absolute;left:0;bottom:0;height:8px;background:var(--renk)}
.kutu{position:absolute;left:130px;right:130px;top:170px}
.cizgi{width:120px;height:8px;border-radius:4px;background:var(--renk);margin:26px 0 34px}
.etiket{display:inline-block;background:var(--renk);color:#0b1020;font-weight:700;font-size:30px;padding:8px 24px;border-radius:999px}
h1{font-size:78px;line-height:1.15;margin-top:26px}
.madde{display:flex;gap:22px;align-items:flex-start;font-size:46px;line-height:1.3;margin-top:30px}
.madde i{flex:none;width:18px;height:18px;border-radius:50%;background:var(--renk);margin-top:22px}
.gizli{visibility:hidden}
.kaynak{position:absolute;left:130px;right:130px;top:800px;font-size:27px;color:#8e97c2}
.satir{display:flex;gap:26px;align-items:center;margin-top:20px;padding:16px 26px;border-radius:18px;
 border:2px solid transparent;font-size:42px;line-height:1.25;opacity:.34}
.satir b{flex:none;width:56px;height:56px;border-radius:50%;background:#2a3158;color:#fff;display:flex;
 align-items:center;justify-content:center;font-size:30px}
.satir.vurgu{opacity:1;background:rgba(255,255,255,.07);border-color:var(--renk)}
.satir.vurgu b{background:var(--renk);color:#0b1020}
.satir.kucuk{font-size:37px;margin-top:12px;padding:12px 24px}
.komut{margin-top:26px;font-family:'DejaVu Sans Mono',monospace;font-size:62px;color:#ffb4b4;background:rgba(239,68,68,.12);
 border:2px solid rgba(239,68,68,.55);border-radius:18px;padding:12px 34px;display:inline-block}
.istek{margin-top:40px;font-size:44px;line-height:1.5;background:rgba(255,255,255,.06);border-left:10px solid var(--renk);
 padding:34px 44px;border-radius:12px}
.orta{position:absolute;left:130px;right:130px;top:300px;text-align:center}
.baslik1{font-size:150px;font-weight:800;line-height:1.1}
.alt1{font-size:58px;color:#c7cdf0;margin-top:26px}
.ozet{font-size:54px;line-height:1.35;font-weight:700}
.sonraki{display:inline-block;margin-top:56px;font-size:38px;color:#aab2d5}
.sonraki b{display:block;font-size:56px;color:#fff;margin-top:10px}
"""


def kare_html(meta, slayt, durum, ilerleme):
    e = html.escape
    renk = meta["renk"]
    soluk = renk + "33"
    govde = ""
    tur = slayt["tur"]
    if tur == "baslik":
        govde = f'<div class="orta"><div class="baslik1">{e(slayt["baslik"])}</div><div class="alt1">{e(slayt["alt"])}</div></div>'
    elif tur == "olay":
        goster = durum.get("goster", len(slayt["maddeler"]))
        maddeler = "".join(
            f'<div class="madde{"" if i < goster else " gizli"}"><i></i><span>{e(m)}</span></div>'
            for i, m in enumerate(slayt["maddeler"])
        )
        govde = (f'<div class="kutu"><span class="etiket">{e(slayt["etiket"])}</span><h1>{e(slayt["baslik"])}</h1>'
                 f'<div class="cizgi"></div>{maddeler}</div>')
        if slayt.get("kaynak"):
            govde += f'<div class="kaynak">{e(slayt["kaynak"])}</div>'
    elif tur == "liste":
        vurgu = durum.get("vurgu", -1)
        vurgular = set(vurgu) if isinstance(vurgu, (list, tuple)) else {vurgu}
        kucuk = " kucuk" if len(slayt["maddeler"]) > 5 else ""
        satirlar = "".join(
            f'<div class="satir{kucuk}{" vurgu" if i in vurgular else ""}"><b>{i + 1}</b><span>{e(m)}</span></div>'
            for i, m in enumerate(slayt["maddeler"])
        )
        govde = f'<div class="kutu"><h1>{e(slayt["baslik"])}</h1><div class="cizgi" style="margin-bottom:10px"></div>{satirlar}</div>'
    elif tur == "komut":
        komutlar = "<br>".join(f'<span class="komut">{e(k)}</span>' for k in slayt["komutlar"])
        govde = (f'<div class="kutu"><h1>{e(slayt["baslik"])}</h1><div class="cizgi"></div>{komutlar}'
                 f'<div class="kaynak" style="position:static;margin-top:34px;font-size:34px;color:#c7cdf0">{e(slayt["alt"])}</div></div>')
    elif tur == "istek":
        govde = f'<div class="kutu"><h1>{e(slayt["baslik"])}</h1><div class="cizgi"></div><div class="istek">{e(slayt["metin"])}</div></div>'
    elif tur == "kapanis":
        govde = (f'<div class="orta"><div class="ozet">{e(slayt["ozet"])}</div>'
                 f'<div class="sonraki">Sıradaki video<b>{e(slayt["sonraki"])}</b></div></div>')
    return (f'<html><head><meta charset="utf-8"><style>:root{{--renk:{renk};--renk-soluk:{soluk}}}{CSS}</style></head><body>'
            f'<div class="glow"></div><div class="ust"><span class="nokta"></span>TANDEM · Yapay Zekâ Eğitimi</div>'
            f'<div class="no">Video {meta["no"]}</div>{govde}'
            f'<div class="ilerleme" style="width:{ilerleme * 100:.1f}%"></div></body></html>')


def kareleri_ciz(meta, durumlar, klasor):
    from playwright.sync_api import sync_playwright
    yollar = {}
    with sync_playwright() as p:
        tarayici = p.chromium.launch(executable_path=os.environ.get("CHROMIUM", "/opt/pw-browsers/chromium"),
                                     args=["--no-sandbox"])
        sayfa = tarayici.new_page(viewport={"width": GEN, "height": YUK})
        for d in durumlar:
            anahtar = d["anahtar"]
            if anahtar in yollar:
                continue
            sayfa.set_content(kare_html(meta, d["slayt"], d, d["ilerleme"]))
            yol = klasor / f"kare_{len(yollar):02d}.png"
            sayfa.screenshot(path=str(yol))
            yollar[anahtar] = yol
        tarayici.close()
    return yollar


# --- ses ---
def _proxy_ayarla():
    proxy = os.environ.get("HTTPS_PROXY")
    ca = Path("/root/.ccr/ca-bundle.crt")
    if proxy and ca.exists():
        import certifi
        certifi.where = lambda: str(ca)     # proxy'nin CA paketi; doğrulama kapatılmaz
    return proxy


async def _seslendir(metinler, klasor, proxy):
    import edge_tts
    sem = asyncio.Semaphore(4)

    async def bir(i, metin):
        async with sem:
            son = None
            for deneme in range(4):
                try:
                    await edge_tts.Communicate(metin, SES, rate=HIZ, pitch=PERDE, proxy=proxy).save(str(klasor / f"{i:03d}.mp3"))
                    return
                except Exception as hata:   # ağ hatası: tekrar dene
                    son = hata
                    await asyncio.sleep(2 * (deneme + 1))
            raise son

    await asyncio.gather(*(bir(i, m) for i, m in enumerate(metinler)))


def wav_oku(yol):
    with wave.open(str(yol), "rb") as w:
        return w.readframes(w.getnframes())


# --- ana akış ---
def video_uret(meta, cikti, sadece_kareler=False):
    cikti.mkdir(parents=True, exist_ok=True)
    gecici = Path(tempfile.mkdtemp(prefix=f"seri2_{meta['no']:02d}_"))
    satirlar, sahne_no = [], []
    for si, sahne in enumerate(meta["sahneler"]):
        for sat in sahne["satirlar"]:
            satirlar.append((si, sahne["slayt"], sat))
    if any(s[1] is None for s in satirlar):
        raise SystemExit(f"Video {meta['no']} için görüntü tanımı (slayt) yok; yalnızca metin hazır.")

    toplam = len(satirlar)
    durumlar = []
    for i, (si, slayt, sat) in enumerate(satirlar):
        d = {"slayt": slayt, "goster": sat.get("goster"), "vurgu": sat.get("vurgu"), "ilerleme": (i + 1) / toplam}
        if d["goster"] is None:
            d.pop("goster")
        if d["vurgu"] is None:
            d.pop("vurgu")
        v = d.get("vurgu")
        d["anahtar"] = (si, d.get("goster"), tuple(v) if isinstance(v, (list, tuple)) else v)
        durumlar.append(d)
    yollar = kareleri_ciz(meta, durumlar, gecici)
    if sadece_kareler:
        for anahtar, yol in yollar.items():
            hedef = cikti / f"kare_{meta['no']:02d}_{yol.name}"
            hedef.write_bytes(yol.read_bytes())
        print("Kontrol kareleri:", cikti)
        return

    # ses
    proxy = _proxy_ayarla()
    metinler = [sat["ses"] or sese_cevir(sat["alt"]) for _, _, sat in satirlar]
    asyncio.run(_seslendir(metinler, gecici, proxy))
    sureler, wavlar = [], []
    for i in range(toplam):
        w = gecici / f"{i:03d}.wav"
        calistir(["ffmpeg", "-v", "error", "-y", "-i", str(gecici / f"{i:03d}.mp3"), "-ar", str(ORNEK_HIZ), "-ac", "1",
                  "-c:a", "pcm_s16le", str(w)])
        wavlar.append(w)
        sureler.append(sure(w))

    # zaman çizelgesi
    t = 0.0
    zaman = []   # (klip_baslangic, ses_baslangic, ses_bitis, klip_bitis)
    for i, dur in enumerate(sureler):
        ses_bas = t + (BAS if i == 0 else 0)
        ses_bit = ses_bas + dur
        if i == toplam - 1:
            bosluk = SON
        else:
            bosluk = BOSLUK_SAHNE if satirlar[i + 1][0] != satirlar[i][0] else BOSLUK_ICERIDE
        zaman.append((t, ses_bas, ses_bit, ses_bit + bosluk))
        t = ses_bit + bosluk
    toplam_sure = t

    # ses dosyası (sessizlik + cümleler, örnek-doğru yerleştirme)
    tampon = bytearray(int(round(toplam_sure * ORNEK_HIZ)) * 2)
    for i, w in enumerate(wavlar):
        veri = wav_oku(w)
        ofset = int(round(zaman[i][1] * ORNEK_HIZ)) * 2
        tampon[ofset:ofset + len(veri)] = veri
    ses_yol = gecici / "ses.wav"
    with wave.open(str(ses_yol), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(ORNEK_HIZ)
        w.writeframes(bytes(tampon))

    # altyazı
    srt = []
    for i, (_, _, sat) in enumerate(satirlar):
        srt.append(f"{i + 1}\n{srt_zaman(zaman[i][1])} --> {srt_zaman(zaman[i][2] + 0.1)}\n{sat['alt']}\n")
    srt_yol = cikti / f"{meta['dosya']}.srt"
    srt_yol.write_text("\n".join(srt), encoding="utf-8")

    # görüntü klipleri: aynı kareyi gösteren ardışık cümleler tek klipte (kinocut create-from-images)
    gruplar = []
    for i, d in enumerate(durumlar):
        if gruplar and gruplar[-1]["anahtar"] == d["anahtar"]:
            gruplar[-1]["bitis"] = zaman[i][3]
        else:
            gruplar.append({"anahtar": d["anahtar"], "baslangic": zaman[i][0], "bitis": zaman[i][3]})
    kliplar = []
    for gi, g in enumerate(gruplar):
        kare_sayisi = round(g["bitis"] * FPS) - round(g["baslangic"] * FPS)
        klip = gecici / f"klip_{gi:02d}.mp4"
        calistir([KINOCUT, "create-from-images", "-f", str(FPS), "-o", str(klip)] + [str(yollar[g["anahtar"]])] * kare_sayisi)
        kliplar.append(klip)
    sessiz = gecici / "sessiz.mp4"
    calistir([KINOCUT, "merge", *map(str, kliplar), "-td", "0", "-o", str(sessiz)])

    seslendi = gecici / "sesli.mp4"
    calistir([KINOCUT, "add-audio", str(sessiz), str(ses_yol), "--duration-policy", "keep_video", "-o", str(seslendi)])
    norm = gecici / "norm.mp4"
    calistir([KINOCUT, "normalize-audio", str(seslendi), "-l", "-16", "--fade-seconds", "0", "-o", str(norm)])
    stil = ("FontName=DejaVu Sans,FontSize=44,PrimaryColour=&H00FFFFFF&,OutlineColour=&H00000000&,"
            "BackColour=&H99000000&,BorderStyle=3,Outline=3,Shadow=0,MarginV=50,Alignment=2")
    altyazili = gecici / "altyazili.mp4"
    calistir([KINOCUT, "subtitles", str(norm), str(srt_yol), "--style", stil, "-o", str(altyazili)])
    final = cikti / f"{meta['dosya']}.mp4"
    calistir([KINOCUT, "fade", str(altyazili), "--fade-in", "0.4", "--fade-out", "0.8", "-o", str(final)])

    print(f"Video {meta['no']}: {final}  ({sure(final):.1f} sn, ses toplamı {sum(sureler):.1f} sn, {len(gruplar)} klip)")
    print("Kalite kontrolü:")
    print(calistir([KINOCUT, "video-quality-check", str(final)]))


def md_yaz():
    satirlar = ["# Seri 2 senaryoları (09–14)\n",
                "Bu dosya `arac/senaryolar.py` içinden otomatik üretilir; düzeltme için o dosyayı değiştir. "
                "Satırlar altyazı metnidir; her satır ekranda ayrı bir altyazı olarak görünür. "
                "Süre tahmini ≈ 2,1 kelime/sn.\n"]
    for v in VIDEOLAR:
        alts = [s["alt"] for sh in v["sahneler"] for s in sh["satirlar"]]
        kelime = len(" ".join(alts).split())
        uretildi = (KOK / "videolar" / f"{v['dosya']}.mp4").exists()
        satirlar.append(f"\n---\n\n## Video {v['no']}: {v['baslik']}\n")
        satirlar.append(f"~{kelime} kelime, yaklaşık {kelime / 2.1 / 60:.1f} dakika. "
                        f"Durum: {'**video üretildi**' if uretildi else 'yalnızca senaryo'}.\n")
        for i, a in enumerate(alts, 1):
            satirlar.append(f"{i}. {a}")
        if v["kaynaklar"]:
            satirlar.append("\n**Kaynaklar**\n")
            satirlar.extend(f"- [{ad}]({url})" for ad, url in v["kaynaklar"])
        if v["notlar"]:
            satirlar.append("\n**Doğrulama notları (neye ne kadar güvenebilirsin)**\n")
            satirlar.extend(f"- {n}" for n in v["notlar"])
    (KOK / "SENARYOLAR.md").write_text("\n".join(satirlar) + "\n", encoding="utf-8")
    print("Yazıldı:", KOK / "SENARYOLAR.md")


def main():
    ap = argparse.ArgumentParser()
    alt = ap.add_subparsers(dest="komut", required=True)
    alt.add_parser("md")
    v = alt.add_parser("video")
    v.add_argument("no", type=int)
    v.add_argument("--kareler", action="store_true", help="yalnızca kontrol karelerini çiz")
    v.add_argument("--cikti", default=str(KOK / "videolar"), help="çıktı klasörü")
    a = ap.parse_args()
    if a.komut == "md":
        md_yaz()
    else:
        meta = next((x for x in VIDEOLAR if x["no"] == a.no), None)
        if not meta:
            raise SystemExit("Bilinmeyen video numarası")
        video_uret(meta, Path(a.cikti), a.kareler)


if __name__ == "__main__":
    main()
