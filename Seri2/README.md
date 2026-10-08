# Seri 2: proje yürütme, standartlar ve yasal zorunluluklar

01–08 videolarının devamı. Araç kurulumu değil; bir projeyi baştan sona yürütürken yapay zekânın çoğu zaman unuttuğu işleri anlatır.

| # | Konu | Durum |
|---|---|---|
| 09 | Git: yapay zekâ çağında kayıt noktası | video üretildi |
| 10 | Ne yapacağına göre doğru yol (dil ve araç haritası) | yalnızca senaryo |
| 11 | Web sitesi yasal zorunlulukları (KVKK, çerez, satış, GDPR) | video üretildi |
| 12 | Mobil ve oyun: mağaza ve platform kuralları | yalnızca senaryo |
| 13 | Yapay zekânın en çok unuttuğu güvenlik ve kalite işleri | yalnızca senaryo |
| 14 | Yayından önce denetim | yalnızca senaryo |

- **`SENARYOLAR.md`**: altı videonun tüm altyazı metni, kaynakları ve "neye ne kadar güvenebilirsin" notları.
- **`videolar/`**: üretilen `.mp4` ve `.srt` dosyaları (mp4'ler Git LFS ile tutulur: `git lfs pull`).
- **`arac/senaryolar.py`**: tek kaynak. Metin ve ekran tasarımı burada; `SENARYOLAR.md` buradan üretilir.
- **`arac/uret.py`**: üretici. Görüntüyü HTML'den çizer, sesi Microsoft Ahmet sinir sesiyle (`edge-tts`) üretir; birleştirme, ses ekleme, ses seviyesi (−16 LUFS), altyazı yakma ve kalite kontrolü [kinocut](https://github.com/KyaniteLabs/kinocut) ile yapılır.

```
pip install kinocut edge-tts playwright pillow    # ayrıca ffmpeg ve bir Chromium
python arac/uret.py md          # SENARYOLAR.md
python arac/uret.py video 9     # videolar/09_*.mp4 + .srt
python arac/uret.py video 9 --kareler --cikti /tmp/kontrol   # yalnızca kontrol kareleri
```

Notlar
- Ses çevrimiçi servistir (`edge-tts`, resmî olmayan yol); metin Microsoft'a gider. Gizli bilgi yazma.
- Metindeki rakamlar ve kaynaklar ikincil kaynaklara (hukuk büroları, haber siteleri) dayanır. Yayından önce `SENARYOLAR.md` içindeki "doğrulama notları" okunmalı; hukuki içerik bir hukukçuya onaylatılmalı.
- Kinocut'un otomatik kalite kontrolü bu videolarda kontrast, doygunluk ve "durağan görüntü" için FAIL verir; koyu zeminli slayt tasarımının doğal sonucudur. Ses seviyesi PASS.
