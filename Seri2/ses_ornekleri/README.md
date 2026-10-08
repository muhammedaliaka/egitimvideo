# Ses örnekleri

Aynı metin farklı ücretsiz seslerle okutuldu. Hangisinin doğal olduğuna sen karar ver; ben ses kalitesini duyamıyorum.

**Türkçe metin:** "Yapay zekâ hızlı çalışır; yanlış yaptığında da hızlı yapar. Bu yüzden projenin ilk işi, geri dönebileceğin bir kayıt noktasıdır. Temmuz 2025'te bir yapay zekâ ajanı, kodu dondurma talimatına rağmen bir şirketin canlı veritabanını sildi."

**İngilizce metin:** "AI works fast, and when it gets something wrong, it gets it wrong fast. That is why the first job of any project is a save point you can always return to. In July 2025, an AI agent deleted a company's live database, despite a code freeze."

| Dosya | Motor | Ses | Dil |
|---|---|---|---|
| `edge_ahmet_tr.mp3` | edge (Microsoft Edge sesli okuma) | Ahmet (erkek, Türkçe) | TR |
| `edge_emel_tr.mp3` | edge | Emel (kadın, Türkçe) | TR |
| `edge_andrew_multi_tr.mp3`, `edge_andrew_multi_en.mp3` | edge | Andrew (çok dilli, erkek) | TR + EN |
| `edge_brian_multi_tr.mp3`, `edge_brian_multi_en.mp3` | edge | Brian (çok dilli, erkek) | TR + EN |
| `edge_ava_multi_tr.mp3`, `edge_ava_multi_en.mp3` | edge | Ava (çok dilli, kadın) | TR + EN |
| `edge_emma_multi_tr.mp3`, `edge_emma_multi_en.mp3` | edge | Emma (çok dilli, kadın) | TR + EN |
| `chatterbox_tr.mp3`, `chatterbox_en.mp3` | chatterbox (yerel, MIT) | varsayılan ses | TR + EN |

Çok dilli sesler Türkçe metni İngilizce telaffuz yapısıyla okuyabilir; en doğal Türkçe için Ahmet ve Emel'i, hem Türkçe hem İngilizce tek ses istiyorsan Chatterbox'ı dinle.

Hız: edge birkaç saniyede üretir. Chatterbox bu bulut makinesinde (GPU yok, CPU) 12 saniyelik Türkçe sesi 78 saniyede üretti ve model yüklemesi ~72 saniye sürdü; GPU'lu bir bilgisayarda çok daha hızlıdır.
