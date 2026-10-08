"""Ücretsiz seslendirme MCP sunucusu (stdio)."""
import asyncio
import json
import os
from pathlib import Path

from mcp.server.fastmcp import FastMCP

from . import motorlar
from .okunus import sese_cevir

mcp = FastMCP("egitim-ses")


def _cikti_yolu(dosya_adi, uzanti):
    klasor = Path(os.environ.get("SES_CIKTI", "ses")).expanduser()
    klasor.mkdir(parents=True, exist_ok=True)
    ad = Path(dosya_adi).stem
    return klasor / f"{ad}{uzanti}"


@mcp.tool()
async def sesleri_listele(dil: str = "tr") -> str:
    """Kullanılabilir ücretsiz sesleri listeler. 'dil' örneği: tr, en. Çok dilli (Multilingual) sesler her dilde gelir."""
    return json.dumps(await motorlar.edge_sesler(dil), ensure_ascii=False)


@mcp.tool()
async def motorlari_denetle() -> str:
    """Hangi ücretsiz motorların bu bilgisayarda hazır olduğunu söyler."""
    return json.dumps({"edge": "çevrimiçi, kurulum gerekmez", "chatterbox": motorlar.chatterbox_var()}, ensure_ascii=False)


@mcp.tool()
async def seslendir(
    metin: str,
    dosya_adi: str,
    motor: str = "edge",
    ses: str = "tr-TR-AhmetNeural",
    dil: str = "tr",
    hiz_yuzde: int = 0,
    referans_ses: str | None = None,
    okunusu_duzelt: bool = True,
) -> str:
    """Metni seslendirip dosyaya yazar ve yolunu döndürür.

    motor: 'edge' (çevrimiçi, ücretsiz) veya 'chatterbox' (yerel, ücretsiz, daha doğal; GPU önerilir).
    ses: yalnızca edge için, örn. tr-TR-AhmetNeural, tr-TR-EmelNeural, en-US-AndrewMultilingualNeural.
    dil: 'tr' veya 'en' (chatterbox için dil kodu).
    hiz_yuzde: -50..+50; edge için konuşma hızı.
    referans_ses: yalnızca chatterbox; 5-15 sn'lik bir .wav verilirse o sesi taklit eder (kendi sesin veya izinli bir ses).
    okunusu_duzelt: Türkçe metinde sayıları yazıya, İngilizce adları okunuşa çevirir.
    """
    metin_ses = sese_cevir(metin) if (okunusu_duzelt and dil.lower().startswith("tr")) else metin
    if motor == "edge":
        yol = _cikti_yolu(dosya_adi, ".mp3")
        await motorlar.edge_uret(metin_ses, yol, ses, hiz_yuzde)
    elif motor == "chatterbox":
        yol = _cikti_yolu(dosya_adi, ".wav")
        await asyncio.to_thread(motorlar.chatterbox_uret, metin_ses, yol, dil, referans_ses)
    else:
        return json.dumps({"hata": "motor 'edge' veya 'chatterbox' olmalı"}, ensure_ascii=False)
    return json.dumps({"dosya": str(yol), "sure_sn": motorlar.sure(yol), "okunan_metin": metin_ses}, ensure_ascii=False)


def main():
    mcp.run()


if __name__ == "__main__":
    main()
