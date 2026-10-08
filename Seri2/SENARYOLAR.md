# Seri 2 senaryoları (09–14)

Bu dosya `arac/senaryolar.py` içinden otomatik üretilir; düzeltme için o dosyayı değiştir. Satırlar altyazı metnidir; her satır ekranda ayrı bir altyazı olarak görünür. Süre tahmini ≈ 2,1 kelime/sn.


---

## Video 9: Git: geri dönebilmenin yolu

~229 kelime, yaklaşık 1.8 dakika. Durum: **video üretildi**.

1. Dokuzuncu video: Git. Yapay zekâ hızlı çalışır; yanlış yaptığında da hızlı yapar. Bu yüzden projenin ilk işi, geri dönebileceğin bir kayıt noktasıdır.
2. Temmuz 2025'te bir yapay zekâ ajanı, kodu dondurma talimatına rağmen bir şirketin canlı veritabanını sildi.
3. Ajan geri almanın imkânsız olduğunu söyledi; yanlıştı, veri geri getirildi. Ders: bu tür iddiayı kendin kontrol et.
4. Ekim 2026'da bir geliştirici forumda anlattı: Cursor'un ajanı, klasör silme komutunu yanlış yazdı.
5. Kaynak kod, Git klasörü ve elle aldığı yedek aynı diskteydi; üçü birden gitti.
6. Yani Git tek başına yetmez: kayıt noktasının bir kopyası, ajanın ulaşamayacağı yerde olmalı.
7. Git, projenin zaman makinesidir. Her kayıt noktasına commit denir; bozulursa son iyi noktaya dönersin. Ama yalnızca kaydettiğin şeyi geri getirir.
8. Birinci kural: göreve başlamadan önce kayıt al. Yapay zekâya yaz: bu klasörde Git başlat ve ilk kayıt noktasını al.
9. İkinci kural: kaydı GitHub gibi uzak bir depoya da gönder. Disk gitse bile proje durur.
10. Üçüncü kural: silme ve sıfırlama komutlarını yapay zekâ ancak senin onayınla çalıştırsın.
11. Ekrandaki komutlardan birini görürsen dur ve hedef yolu kendin oku.
12. Dördüncü kural: parola ve anahtar Git'e girmez. GitGuardian'ın 2026 raporuna göre, yapay zekâ destekli commit'lerde sızıntı ortalamanın yaklaşık iki katı. Sızan anahtarı silmek yetmez; değiştirmen gerekir.
13. Beşinci kural: bozulunca yapay zekâyı durdur ve o diske yazma; son kayıt noktasına ve uzak depoya bak.
14. Özet: kayıt al, uzağa gönder, silme komutunu oku, anahtarı sakla. Sıradaki video: ne yapacağına göre doğru yol.

**Kaynaklar**

- [Replit olayı, Temmuz 2025 (The Register)](https://www.theregister.com/2025/07/22/replit_saastr_response/)
- [Replit olayı kaydı (AI Incident Database)](https://incidentdatabase.ai/fr/entities/replit-ai-agent/)
- [Cursor olayı, 3 Ekim 2026 (kullanıcının kendi anlatımı)](https://forum.cursor.com/t/errible-ai-out-of-control-randomly-deleting-files-6-month-project-wiped-out/173688)
- [GitGuardian Secrets Sprawl 2026](https://gitguardian.com/state-of-secrets-sprawl-report-2026)

**Doğrulama notları (neye ne kadar güvenebilirsin)**

- Replit (Temmuz 2025): birden çok haber aynı çekirdeği anlatıyor; ayrıntılar (kayıt sayısı, ajanın 'sahte veri' üretmesi) kaynaklar arasında değişiyor, videoya yalnızca ortak olanı koydum.
- Cursor (3 Ekim 2026): tek kullanıcının anlatımı; sebep (model mi, komut hatası mı) kanıtlı değil, uzak depo olup olmadığı yazılmamış. Videoda 'kullanıcı anlattı' diye geçiyor.
- GitGuardian: rapor tam metni okunamadı; yüzde 3,2'ye karşı 1,5 oranı basın bülteninden. Kapsam (yalnızca Claude Code mu, tüm yapay zekâ destekli commit'ler mi) kaynaklarda tartışmalı; videoda yalnızca 'yaklaşık iki kat' deniyor.
- Antigravity D: diski (Kasım 2025) ve Claude Code ev klasörü (Aralık 2025) olayları tek kullanıcı anlatımı olduğu ve Git kullanılıp kullanılmadığı yazılmadığı için videoya girmedi.
- Git'in 'kurtardığı' doğrulanmış tek bir hikâye bulamadım; video bunu olay olarak değil, çalışma mantığı olarak anlatıyor.

---

## Video 10: Ne yapacağına göre doğru yol

~236 kelime, yaklaşık 1.9 dakika. Durum: yalnızca senaryo.

1. Onuncu video: ne yapacağına göre doğru yol. Yapay zekâya “hangi dille yapayım” diye sormadan önce üç şeyi söylemelisin: ne yapıyorsun, kim kullanacak, nerede çalışacak.
2. Web sitesi ya da web uygulaması: HTML, CSS ve JavaScript ya da TypeScript. Üstüne React, Vue ya da Svelte gibi bir çerçeve; sunucu için Node ya da Python.
3. Küçük bir tanıtım sitesi için çerçeveye gerek yok. Düz HTML ve CSS yeter; daha az parça, daha az hata.
4. Mobil uygulama: iPhone için Swift, Android için Kotlin. İkisini tek kodla istersen Flutter ya da React Native.
5. Masaüstü uygulama: Windows için C# ve .NET; her sistemde çalışsın istersen Electron ya da Tauri.
6. Ama önce şunu sor: bu iş bir web uygulamasıyla çözülmüyor mu? Çoğu zaman çözülür ve bakımı çok daha kolaydır.
7. Oyun: Unity C# ile, Unreal C++ ve Blueprint ile, Godot GDScript ile yazılır. Roblox'ta dil Luau.
8. Seçerken üç kural. Bir: yaygın olanı seç. Yapay zekâ, çok örneği olan teknolojide çok daha iyi çalışır.
9. İki: tek yığın kullan. Bir projede iki dil ve iki çerçeve, hata sayısını katlar.
10. Üç: sürümü yazdır ve resmî belgeden doğrulat. Yapay zekânın bilgisi eskiyebilir.
11. Her dilin standart araçları vardır: biçimlendirici, hata denetçisi ve test aracı. İlk günden kurdur; kalite buradan başlar.
12. Kararı karar defterine yaz: neden bu dil, neden bu çerçeve. Altı ay sonra kimse hatırlamaz.
13. İstek örneği: şunu yapacağım. Üç yığın öner. Artısını, eksisini ve bu projeye uyumunu yaz. Resmî belgeden doğrula.
14. Sıradaki video: web sitesi yapıyorsan yasal zorunluluklar.

**Doğrulama notları (neye ne kadar güvenebilirsin)**

- Bu videodaki dil ve araç eşleşmeleri yaygın, yerleşik seçimlerdir; sürüm numarası verilmedi. Yayın öncesi resmî belgeden doğrulanmalı (videoda da söyleniyor).
- Bu video için henüz ayrıca web araştırması yapılmadı; üretilmeden önce 'en yaygın yığın' ifadeleri güncel kaynakla (ör. yıllık geliştirici anketleri) desteklenebilir.

---

## Video 11: Web sitesi yapıyorsan: yasal zorunluluklar

~234 kelime, yaklaşık 1.9 dakika. Durum: yalnızca senaryo.

1. On birinci video: yasal zorunluluklar. Yapay zekâ siteyi bir saatte yapar; yasal metinleri çoğu zaman sen istemedikçe düşünmez.
2. Önce şunu bil: siteyi yapay zekânın yapmış olması cezayı değiştirmez; sorumlu site sahibidir. Örneklerde ceza, eksik metne kesiliyor.
3. Türkiye'de ilk kural: kişisel veri topladığın her yerde aydınlatma metni; kim topluyor, ne amaçla, kime aktarılıyor, kullanıcının hakları ne.
4. Eksik bırakmanın 2026 cezası, kaynaklara göre 85.437 ile 1.709.200 lira arasında; her yıl yeniden değerleme oranıyla artıyor.
5. İkinci kural: çerezler. Zorunlu olmayan çerezlerde, yani analitik ve reklamda, çerez yerleşmeden önce açık rıza gerekir.
6. Kabul, reddet ve tercihler düğmeleri eşit görünmeli. “Siteyi kullanmaya devam ederek kabul etmiş sayılırsınız” rıza değildir.
7. Üçüncü kural: para alıyorsan, mesafeli satış sözleşmesi, ön bilgilendirme, cayma ve iade koşulları sitede yazılı olmalı.
8. Kendi alan adından satış yapıyorsan ETBİS kaydı gerekir. Reklam e-postası ya da SMS göndereceksen önce onay al ve İYS'ye kayıt ol.
9. Avrupa'dan ziyaretçin varsa GDPR devreye girer: tavan ceza yirmi milyon avro ya da yıllık cironun yüzde dördü.
10. 2025'te Fransa'nın veri koruma kurumu, çerezler yüzünden Shein'e 150 milyon, Google'a 325 milyon avro kesti.
11. Küçük siteler de kurtulmadı: İspanya'da bir online mağaza, yetersiz gizlilik metni yüzünden 6.000 avro ödedi.
12. Yapay zekâya yaz: bu site hangi kişisel verileri topluyor? Türkiye ve Avrupa için hangi yasal metinler gerekir? Resmî kaynağı göster.
13. Metinleri yapay zekâ taslak olarak yazar; son hâlini bir hukukçu onaylamalı. Bu video bilgilendirme amaçlıdır, hukuki danışmanlık değildir.
14. Sıradaki video: mobil uygulama ve oyunlarda mağaza kuralları.

**Kaynaklar**

- [KVKK 2026 idari para cezası tutarları (Cott Group)](https://www.cottgroup.com/tr/mevzuat/item/yeniden-degerleme-oranina-gore-2026-yili-kvkk-idari-para-cezalari)
- [KVKK 2026 idari para cezaları (Mondaq)](https://www.mondaq.com/turkey/data-protection/1726256/2026-y%C4%B1l%C4%B1-kvkk-%C4%B0dari-para-cezalar%C4%B1-g%C3%BCncel-tutarlar-ve-uyar%C4%B1lar)
- [KVKK çerez rehberi güncellemesi (Erdem & Erdem)](https://www.erdem-erdem.av.tr/bilgi-bankasi/kisisel-verileri-koruma-kurumu-cerez-uygulamalari-hakkinda-rehberi-guncelledi)
- [E-ticaret siteleri hukuki yükümlülükler 2026 (FFK Partner)](https://www.ffkpartnerhukuk.com.tr/e-ticaret-sitelerinin-hukuki-yukumlulukleri-2026-guncel-rehber/)
- [İYS kayıt yükümlülüğü (Moroğlu Arseven)](https://www.morogluarseven.com/insights/publications/articles-en/guide-on-commercial-electronic-communication-management-system/)
- [CNIL: Google 325 M€, Shein 150 M€ (Privacy Laws & Business)](https://www.privacylaws.com/news/cnil-fines-google-325-million-and-shein-150-million/)
- [İspanya, yetersiz gizlilik metni cezası (MLex)](https://www.mlex.com/mlex/articles/2248536/unnamed-website-owner-pays-gdpr-fine-over-deficient-privacy-policy)

**Doğrulama notları (neye ne kadar güvenebilirsin)**

- Önemli: 'Yapay zekâyla yapılan siteye ceza kesildi' diye belgelenmiş bir yaptırım bulamadım. Bulduğum örneklerde ceza eksik/yetersiz gizlilik metnine kesiliyor; sitenin hangi araçla yapıldığı konu değil. Video bu yüzden 'araç fark etmez, sorumlu site sahibi' diyor.
- KVKK ceza bandı (85.437 – 1.709.200 TL) ikincil kaynaklardan (hukuk büroları); dayanak olarak gösterilen yeniden değerleme oranı %25,49 (Resmî Gazete 27.11.2025, sayı 33090). Resmî kaynaktan teyit edilmeli.
- KVKK çerez rehberi 2025'te güncellenmiş (videoya girmedi; eski 2022 yazılarına güvenme). Rehber tavsiye niteliğinde; 'eşit görünür düğmeler' ve 'devam etmek rıza değildir' ilkeleri ikincil kaynaklardan. Rehberin 2025 güncellemesi metni doğrudan okunamadı.
- ETBİS ve İYS ayrıntıları hukuk bürosu yazılarından; ETBİS tebliğinin yürürlük tarihi kaynaklar arasında 1 ve 11 Ağustos 2017 diye ayrışıyor (videoda tarih yok).
- GDPR tavanı (20 milyon € ya da %4) kanun metninden bilinen üst sınır; ceza bunun altında verilir. İspanya örneği MLex haberinden; resmî karar metni okunmadı.
- Bu video hukuki danışmanlık değildir; videonun sonunda da söyleniyor. Yayından önce bir hukukçu onaylamalı.

---

## Video 12: Mobil ve oyun: mağaza ve platform kuralları

~239 kelime, yaklaşık 1.9 dakika. Durum: yalnızca senaryo.

1. On ikinci video: mağaza ve platform kuralları. Uygulamanın ya da oyunun çalışması yetmez; mağaza onaylamalı. Kurallar sık değişir, buradaki bilgileri yayından önce resmî sayfadan doğrula.
2. Apple: kullanıcı hesap açabiliyorsa, uygulamanın içinden hesabı silme seçeneği şart. Hesabı yalnızca dondurmak yetmez.
3. Apple ile giriş sunuyorsan, hesap silinirken Apple'ın erişim anahtarını da iptal etmelisin.
4. Google Play: gizlilik politikası zorunlu. Veri güvenliği formu da zorunlu; eksikse uygulama yayınlanmaz ya da güncellenemez.
5. Google da hesap silmeyi ister: uygulamanın içinde ve web'de bulunabilir olmalı. Verinin kendisi de silinmeli.
6. 31 Ağustos 2026'dan beri yeni uygulama ve güncellemeler Android 16'yı, yani API 36'yı hedeflemeli.
7. 2023 Kasım'ından sonra açılan kişisel Google hesaplarında, yayından önce on iki test kullanıcısıyla on dört gün kapalı test şartı var.
8. Steam: oyun başına yüz dolar ücret. Yapay zekâ içeriği varsa bildirmek gerekir: oyunda görünen ya da oyun sırasında üretilen içerik. Kaynaklara göre kod yazmak için kullandığın araçlar bildirilmez.
9. Roblox, TANDEM'in platformu. 2026'da yaş doğrulaması sıkılaştı: sohbet için yaş kontrolü; tüm yaşlara açık yayın için kimlik doğrulama, iki adımlı doğrulama, abonelik ve oyun incelemesi.
10. Her deneyim için yaş anketini doldurmazsan, on üç yaş altına gösterilmez. Güncel şartları Creator Docs sayfasından kontrol et.
11. Çocuklara yönelik her şeyde kurallar daha sıkı: yaş derecesi, veri toplama, reklam. Çocuk kullanıcı ihtimali varsa baştan planla.
12. İstek örneği: bu uygulamayı Apple, Google ve Steam'e yüklemeden önce kontrol listesi çıkar. Her madde için resmî sayfanın bağlantısını ve bugünün tarihini yaz.
13. Sıradaki video: yapay zekânın en çok unuttuğu güvenlik ve kalite işleri.

**Kaynaklar**

- [Google Play: hesap silme ve veri güvenliği formu (Hunton, Help Net Security)](https://www.helpnetsecurity.com/?p=259913)
- [Google Play kapalı test şartı (Google Play Console Yardım)](https://support.google.com/googleplay/android-developer/answer/14151465)
- [Android hedef API şartı (Android Developers)](https://developer.android.com/google/play/requirements/target-sdk)
- [Apple: uygulama içi hesap silme (App Store Review Guidelines 5.1.1(v))](https://developer.apple.com/app-store/review/guidelines/#5.1.1)
- [Steam AI bildirimi (Valve ocak 2026, ikincil kaynaklar)](https://www.prismnews.com/hobbies/video-games/valve-clarifies-steam-ai-disclosure-rules-internal-tools-exempt-content-disclosed)
- [Steamworks uygulama ücreti](https://partner.steamgames.com/doc/gettingstarted/appfee)
- [Roblox yayın şartları (Creator Docs)](https://create.roblox.com/docs/production/publishing/kids-and-select)

**Doğrulama notları (neye ne kadar güvenebilirsin)**

- Google'ın 'API 36' şartı: arama sonuçları 31 Ağustos 2026 tarihli şartı gösteriyor; eski yazılar API 35 diyor. Yayın öncesi resmî sayfadan doğrula.
- 12 test kullanıcısı / 14 gün şartı: yalnızca 13 Kasım 2023 sonrası açılan KİŞİSEL hesaplar için; kurumsal hesapların muaf olduğu bilgisi üçüncü taraf kaynaklarda, resmî sayfada teyit edilmedi.
- Steam: video 'kod asistanları bildirilmez' diyor; bu bilgi ikincil haber kaynaklarından (Valve'in ocak 2026 güncellemesi). Resmî Steamworks sayfası açılamadı.
- Roblox yayın şartları 2026'da birkaç kez değişti (mayıs/haziran uygulamaları); TANDEM için yayından önce Creator Docs kontrol edilmeli. Güncel durum doğrulanmadı.

---

## Video 13: Yapay zekânın en çok unuttuğu güvenlik ve kalite işleri

~253 kelime, yaklaşık 2.0 dakika. Durum: yalnızca senaryo.

1. On üçüncü video: yapay zekânın en çok unuttuğu işler. Veracode'un Temmuz 2026 raporuna göre, yapay zekâ kodunun güvenlik testini geçme oranı ortalama yüzde elli altı. Sözdizimi neredeyse kusursuz; güvenlik değil.
2. Rapordaki istemlerde güvenlik talimatı yoktu. Yani güvenliği sen istemezsen, çoğu zaman o da düşünmez.
3. Bir: yetki. Lovable ve Supabase ile yapılan uygulamalarda satır düzeyinde yetki kapalı geliyordu; 2025'te yüz yetmişten fazla uygulama açıkta kaldı.
4. 2026'da UpGuard, herkese açık tabloları olan 16.326 Supabase veritabanı saptadı; yarısından fazlasında kişisel veri belirtisi vardı.
5. Test: kendi anahtarınla başka bir kullanıcının verisini okuyabiliyor musun? Okuyabiliyorsan açık var.
6. İki: uydurma paket. Bir araştırmada yapay zekâ örneklerinin yaklaşık yüzde yirmisi, var olmayan bir paket adı önerdi; uydurmaların yüzde kırk üçü her seferinde tekrarlandı.
7. Saldırgan o adla bir paket yayınlayıp bekler. Önerilen paketi kurmadan önce bak: kim yayınlamış, kaç indirmesi var, resmî mi?
8. OWASP'ın 2025 listesinde ilk üç sırada yetki, yanlış yapılandırma ve yazılım tedarik zinciri var. Gizli anahtarları dokuzuncu videoda konuştuk.
9. Dört: erişilebilirlik. Avrupa Erişilebilirlik Yasası 28 Haziran 2025'ten beri uygulanıyor. Avrupa'daki kullanıcıya hizmet veren web siteleri, mobil uygulamalar ve e-ticaret kapsamda.
10. Teknik ölçüt EN 301 549, yani WCAG 2.1 AA seviyesi. Yapay zekâya klavyeyle kullanımı, renk karşıtlığını ve resim açıklamalarını kontrol ettir.
11. Küçük hizmet sağlayıcılar için muafiyet var ama dar. Kendi durumunu doğrulat.
12. Beş: yedek ve test. Yapay zekâya test yazdır ve çalıştırt. Yedeği de geri yükleyerek dene; denenmemiş yedek, yedek değil varsayımdır.
13. İstek örneği: bu projeyi bir saldırgan gibi incele. Her bulgu için dosyayı, satırı ve düzeltmeyi yaz. Emin olmadıklarını işaretle.
14. Sıradaki video: yayından önce tek komutla denetim.

**Kaynaklar**

- [Veracode 2026 raporu özeti (Let's Data Science)](https://letsdatascience.com/news/veracode-finds-ai-code-security-stalled-at-56-616847d8)
- [Lovable / Supabase RLS, CVE-2025-48757](https://blog.vibecoder.me/post-mortem-lovable-cve-2025-48757)
- [16.000+ Supabase veritabanı açık (Cybernews)](https://cybernews.com/news/16000-supabase-databases-exposed/)
- [Uydurma paket / slopsquatting (SD Times)](https://sdtimes.com/coding-assistants/hallucinated-code-real-threat-how-slopsquatting-targets-ai-assisted-development/)
- [OWASP Top 10:2025](https://owasp.org/Top10/2025/)
- [Avrupa Erişilebilirlik Yasası (Avrupa Komisyonu erişilebilirlik merkezi)](https://accessible-eu-centre.ec.europa.eu/content-corner/news/eaa-comes-effect-june-2025-are-you-ready-2025-01-31_en)

**Doğrulama notları (neye ne kadar güvenebilirsin)**

- Veracode: 2026 raporunda güvenlik testi geçme oranı ortalama %56 (2025'te ~%45 açıklı). Raporun istemlerinde güvenlik talimatı yoktu; bu yüzden videoda 'sen istemezsen çoğu zaman düşünmez' deniyor, 'her kod %44 açıklı' denmiyor. Birincil rapor okunmadı.
- Lovable/Supabase: 170+ uygulama (CVE-2025-48757) ve UpGuard'ın 16.326 veritabanı bulgusu satıcı/haber kaynaklarından; sayılar kaynaklar arasında değişiyor.
- Uydurma paket: USENIX 2025 çalışması (örneklerin ~%20'si olmayan paket, %43'ü tekrarlıyor) ikincil özetten; birincil makale okunmadı.
- Erişilebilirlik muafiyeti (10 çalışan altı, 2 milyon € altı) hizmet sağlayıcı mikro işletmeler için; kaynaklar bu ayrımı net yazmıyor, video 'kendi durumunu doğrulat' diyor. Ceza tutarları ülkeye göre; rakam verilmedi.

---

## Video 14: Yayından önce denetim

~199 kelime, yaklaşık 1.6 dakika. Durum: yalnızca senaryo.

1. Son video: yayından önce denetim. Yapay zekâ ekibin en hızlı üyesi. Unuttuklarını ise bir listeyle yakalarsın.
2. Yayın kapısında on soru var. Bir: Git'te son kayıt ve uzak depoda bir kopya var mı?
3. İki: kodda parola ya da anahtar kalmış mı? Üç: yetki testini yaptım mı?
4. Dört: kişisel veri topluyor muyum? Aydınlatma, gizlilik ve çerez metinleri hazır mı? Beş: kullanıcılarım hangi ülkelerde?
5. Altı: çocuk kullanıcı olabilir mi? O zaman kurallar sıkılaşır. Yedi: mağaza ya da platform formları, hesap silme ve yaş derecesi tamam mı?
6. Sekiz: bağımlılıklar gerçek, güncel ve lisansı uygun mu? Dokuz: erişilebilirlik temel kontrolleri yapıldı mı?
7. On: yedeği geri yüklemeyi denedim mi? Hata izleme ve geri dönüş planı var mı?
8. Bunların hepsini tek komutla yapay zekâya denetlet. Proje türünü ve kullanıcı ülkelerini yaz.
9. Çıktı bir tablo olsun: bulgu, kanıt, risk, düzeltme. Kanıt; dosya ve satır ya da resmî kaynak bağlantısı olsun.
10. Doğrulayamadığı her şeye “doğrulanmadı” yazsın. Tahmini, kesin gibi sunmasın.
11. Sonra bulguları sen dene. Hukuki metinleri bir hukukçu onaylasın; yayın kararı proje sahibinin.
12. Yayından sonra da bitmiyor: ceza tutarları her yıl güncelleniyor, mağaza kuralları sık değişiyor. Yılda iki kez yeniden denetle.
13. Özet: kayıt al, yolu seç, yasal metinleri koy, mağaza kurallarını oku, güvenliği ölç, yayından önce denetle. Başarılar!

**Doğrulama notları (neye ne kadar güvenebilirsin)**

- Bu video 09-13'ün özetidir; yeni olgu içermiyor, o yüzden ayrıca kaynak yok. Kontrol listesindeki her madde önceki videolardaki bir bulguya bağlı.
