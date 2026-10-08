"""Türkçe sesin İngilizce adları ve sayıları doğru okuması için metin düzeltmeleri.

Altyazıda doğru yazılış kalır; yalnızca seslendirilen metin bu dosyayla değişir.
"""
import re

SOZLUK = [
    (r"GitGuardian", "Git Gardiyın"), (r"GitHub", "Git Hab"), (r"commit", "komit"),
    (r"Cursor", "Körsır"), (r"Shein", "Şiin"), (r"Google Play", "Gugıl Pley"), (r"Google", "Gugıl"),
    (r"ETBİS", "E Te Bi İs"), (r"İYS", "İ Ye Es"), (r"KVKK", "Ka Ve Ka Ka"), (r"GDPR", "Ge De Pe Er"),
    (r"Roblox", "Robloks"), (r"Veracode", "Verakod"), (r"Supabase", "Süpabeys"), (r"Lovable", "Lavıbıl"),
    (r"UpGuard", "Apgard"), (r"OWASP", "Ovasp"), (r"WCAG", "Ve Ce A Ge"),
    (r"EN 301 549", "E En üç yüz bir beş yüz kırk dokuz"),
    (r"API 36", "A Pe İ otuz altı"), (r"Android 16", "Android on altı"), (r"Apple", "Epıl"), (r"Steam", "Stim"),
    (r"Creator Docs", "Kriyeytır Doks"), (r"Luau", "Lu-au"), (r"Unity", "Yuniti"), (r"Unreal", "Anriıl"),
    (r"Godot", "Godo"), (r"Swift", "Svift"), (r"Kotlin", "Kotlin"), (r"Flutter", "Flatır"),
    (r"React Native", "Riyakt Neytiv"), (r"React", "Riyakt"), (r"Electron", "Elektron"), (r"Tauri", "Tavri"),
    (r"TypeScript", "Tayp Skript"), (r"JavaScript", "Cava Skript"), (r"HTML", "Ha Te Em El"), (r"CSS", "Ce Es Es"),
    (r"Python", "Paython"), (r"Vue", "Vyu"), (r"Svelte", "Svelt"), (r"Blueprint", "Blupırint"),
    (r"GDScript", "Ge Di Skript"), (r"TANDEM", "Tandem"),
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
    """Türkçe metindeki İngilizce adları okunuşa, sayıları yazıya çevirir."""
    for kalip, yeni in SOZLUK:
        metin = re.sub(kalip, yeni, metin)
    return re.sub(r"\d{1,3}(?:\.\d{3})+|\d+", lambda m: tr_sayi(int(m.group(0).replace(".", ""))), metin)
