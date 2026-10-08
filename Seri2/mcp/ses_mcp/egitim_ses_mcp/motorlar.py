"""Seslendirme motorları. İkisi de ücretsizdir.

edge       Microsoft Edge "sesli oku" sinir sesleri. Çevrimiçi, kayıt ve ücret yok; resmî olmayan yoldur.
           Metin Microsoft sunucusuna gider. Türkçe için tr-TR-AhmetNeural / EmelNeural ve çok dilli sesler.
chatterbox Resemble AI Chatterbox Multilingual (MIT). Tamamen yerel, 23 dil (Türkçe dahil), isteğe bağlı ses klonlama.
           GPU yoksa yavaştır. Kurulum: pip install "egitim-ses-mcp[yerel]".
"""
import asyncio
import os
import subprocess
from pathlib import Path


def _proxy():
    """Bulut ortamında proxy CA'sını kullanır; doğrulama kapatılmaz."""
    proxy = os.environ.get("HTTPS_PROXY")
    ca = Path("/root/.ccr/ca-bundle.crt")
    if proxy and ca.exists():
        import certifi
        certifi.where = lambda: str(ca)
    return proxy


def _hiz(yuzde):
    return f"{int(yuzde):+d}%"


async def edge_uret(metin, cikti, ses, hiz_yuzde=0):
    import edge_tts
    proxy = _proxy()
    son = None
    for deneme in range(4):
        try:
            await edge_tts.Communicate(metin, ses, rate=_hiz(hiz_yuzde), proxy=proxy).save(str(cikti))
            return cikti
        except Exception as hata:  # ağ hatası: tekrar dene
            son = hata
            await asyncio.sleep(2 * (deneme + 1))
    raise RuntimeError(f"Edge sesi üretilemedi: {son!r}")


async def edge_sesler(dil):
    import edge_tts
    sesler = await edge_tts.list_voices(proxy=_proxy())
    return [
        {"ad": v["ShortName"], "cinsiyet": v["Gender"], "yerel": v["Locale"]}
        for v in sesler
        if v["Locale"].lower().startswith(dil.lower()) or "Multilingual" in v["ShortName"]
    ]


_chatterbox = {}


def chatterbox_uret(metin, cikti, dil="tr", referans_ses=None):
    """Chatterbox ile yerelde üretir. Çıktı .wav olmalıdır."""
    import torch
    import torchaudio
    if "model" not in _chatterbox:
        from chatterbox.mtl_tts import ChatterboxMultilingualTTS
        cihaz = "cuda" if torch.cuda.is_available() else "cpu"
        _chatterbox["model"] = ChatterboxMultilingualTTS.from_pretrained(device=cihaz)
    m = _chatterbox["model"]
    kw = {"audio_prompt_path": referans_ses} if referans_ses else {}
    wav = m.generate(metin, language_id=dil, **kw)
    torchaudio.save(str(cikti), wav, m.sr)
    return cikti


def chatterbox_var():
    try:
        import chatterbox  # noqa: F401
        import torch
        return {"kurulu": True, "cuda": bool(torch.cuda.is_available())}
    except Exception as hata:
        return {"kurulu": False, "neden": repr(hata)[:120]}


def sure(dosya):
    c = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(dosya)],
        capture_output=True, text=True,
    )
    try:
        return round(float(c.stdout.strip()), 2)
    except ValueError:
        return None
