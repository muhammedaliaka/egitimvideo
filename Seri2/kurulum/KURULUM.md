# Kurulum: yalnızca ücretsiz araçlar

`mcpServers.json`, Claude Desktop yapılandırmandaki `mcpServers` bloğunun güncel hâlidir. Eski hâline iki sunucu eklendi: `egitim-ses` (seslendirme) ve `playwright` (kanıt ekran görüntüsü). Diğer yedi sunucuya dokunulmadı. Hepsi ücretsiz; hesap, kredi kartı ya da API anahtarı gerekmez.

## 1. Yapılandırmayı güncelle

1. Bu depoyu (`egitimvideo`) bilgisayarına indir. `Seri2\mcp\ses_mcp` klasörü ses sunucusunun kendisidir.
2. Claude Desktop → Ayarlar → Geliştirici → Yapılandırmayı Düzenle.
3. Dosyadaki `"mcpServers": { ... }` bloğunu `mcpServers.json` içindekiyle değiştir. `coworkUserFilesPath` ve `preferences` bölümlerine dokunma.
4. `egitim-ses` içindeki `BURAYA_PROJE_KLASORU` yazısını deponun bilgisayarındaki yoluyla değiştir (örn. `C:\\Users\\Muhammed_ali\\Desktop\\egitimvideo`).
5. `C:\Users\Muhammed_ali\Claude\egitim_videolari\ses` ve `...\kanit` klasörlerini oluştur.
6. Claude Desktop'u tamamen kapatıp aç.

Gereksinim: Chrome kurulu olmalı (Playwright onu kullanır); `npx` için Node.js; `uvx` için zaten kurulu olan uv; ses için FFmpeg (süre ölçmek için).

## 2. Ne işe yarıyorlar

| Araç | Lisans | Ne yapar |
|---|---|---|
| `egitim-ses` (bu depoda) | MIT | `seslendir`, `sesleri_listele`, `motorlari_denetle`. Ücretsiz iki motor: **edge** (Microsoft Edge sinir sesleri, çevrimiçi) ve **chatterbox** (yerel, MIT, Türkçe dahil 23 dil, ses klonlama). |
| `playwright` | Apache-2.0 | Gerçek web sayfasını açıp ekran görüntüsü alır; videolardaki "kaynak kanıtı" görüntüleri için. |
| `kinocut` (zaten kurulu) | Apache-2.0 | Ses seviyesi, birleştirme, altyazı yakma. |

## 3. Montaj: HyperFrames (MCP değil, ücretsiz eklenti)

Kinocut'tan güçlü, doğrulanmış bir **montaj MCP'si bulamadım.** Videoyu "yapay" gösteren şey araç değil, görüntüyü kurma biçimiydi (durağan slayt). HyperFrames (HeyGen, Apache-2.0, yerelde render, ücret yok) HTML ve GSAP ile hareketli sahne, kaydırmalı ekran görüntüsü ve altyazı animasyonu yapar. MCP sunucusu yoktur; Claude Code eklentisi ve komut satırı olarak çalışır.

Gereksinim: Node.js 22 veya üstü, FFmpeg.

```
claude plugin marketplace add heygen-com/hyperframes
claude plugin install hyperframes@hyperframes
```

Yalnızca yetenek paketi: `npx skills add heygen-com/hyperframes`. HyperFrames'in HeyGen bulutunda render seçeneği ücretlidir; kullanma, yerel render ücretsizdir.

## 4. Dürüst notlar

- **Ücretli servisleri çıkardım.** ElevenLabs'in ücretsiz planında yardım sayfasına göre ticari kullanım hakkı yok ve atıf gerekiyor; bu yüzden config'e koymadım.
- **Edge sesi ücretsiz ama resmî değil:** Microsoft'un tarayıcıdaki "sesli oku" uç noktasını kullanır; metin Microsoft sunucusuna gider. Gizli bilgi yazma. Türkçe için yalnızca Ahmet ve Emel var; çok dilli sesler (Andrew, Ava, Brian, Emma) Türkçe metni de okur.
- **Chatterbox yerelde çalışır, internet gerektirmez** ama ilk kullanımda ~3 GB model indirir. GPU yoksa çok yavaştır: bu bulutta CPU ile 12 saniyelik Türkçe sesi 78 saniyede, model yüklemesini ayrıca 72 saniyede yaptı. Kurulum: `uvx --from "...\ses_mcp[yerel]" egitim-ses-mcp` (config'deki `args` içindeki yola `[yerel]` ekle).
- **Ses kalitesini duyamıyorum.** Hangisinin doğal olduğuna sen karar ver; bunun için `Seri2/ses_ornekleri/` klasörüne aynı metni farklı seslerle okuttum (liste oradaki README'de).
- Windows yollarını ve Claude Desktop'ta açılışı bu ortamda deneyemedim. Sunucuları Linux'ta `uvx` ile başlatıp araç listesini aldım, ses sunucusuyla gerçekten ses ürettim.
