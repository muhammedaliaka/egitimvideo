"""Seri 2 senaryoları (09-14). Tek kaynak: SENARYOLAR.md ve videolar buradan üretilir.

Her satır (cue): alt = ekranda görünen altyazı, ses = (isteğe bağlı) seslendirme metni.
`ses` verilmezse altyazı okunur; İngilizce adlar `uret.py` içindeki SOZLUK ile okunuşa çevrilir.
slayt: görüntü tanımı (yalnızca üretilen videolar için; None ise yalnızca metin).
"""


def c(alt, ses=None, **kw):
    return {"alt": alt, "ses": ses, **kw}


V09 = {
    "no": 9,
    "dosya": "09_Git_kayit_noktasi",
    "baslik": "Git: geri dönebilmenin yolu",
    "renk": "#f59e0b",
    "sonraki": "Ne yapacağına göre doğru yol",
    "kaynaklar": [
        ("Replit olayı, Temmuz 2025 (The Register)", "https://www.theregister.com/2025/07/22/replit_saastr_response/"),
        ("Replit olayı kaydı (AI Incident Database)", "https://incidentdatabase.ai/fr/entities/replit-ai-agent/"),
        ("Cursor olayı, 3 Ekim 2026 (kullanıcının kendi anlatımı)", "https://forum.cursor.com/t/errible-ai-out-of-control-randomly-deleting-files-6-month-project-wiped-out/173688"),
        ("GitGuardian Secrets Sprawl 2026", "https://gitguardian.com/state-of-secrets-sprawl-report-2026"),
    ],
    "notlar": [
        "Replit (Temmuz 2025): birden çok haber aynı çekirdeği anlatıyor; ayrıntılar (kayıt sayısı, ajanın 'sahte veri' üretmesi) kaynaklar arasında değişiyor, videoya yalnızca ortak olanı koydum.",
        "Cursor (3 Ekim 2026): tek kullanıcının anlatımı; sebep (model mi, komut hatası mı) kanıtlı değil, uzak depo olup olmadığı yazılmamış. Videoda 'kullanıcı anlattı' diye geçiyor.",
        "GitGuardian: rapor tam metni okunamadı; yüzde 3,2'ye karşı 1,5 oranı basın bülteninden. Kapsam (yalnızca Claude Code mu, tüm yapay zekâ destekli commit'ler mi) kaynaklarda tartışmalı; videoda yalnızca 'yaklaşık iki kat' deniyor.",
        "Antigravity D: diski (Kasım 2025) ve Claude Code ev klasörü (Aralık 2025) olayları tek kullanıcı anlatımı olduğu ve Git kullanılıp kullanılmadığı yazılmadığı için videoya girmedi.",
        "Git'in 'kurtardığı' doğrulanmış tek bir hikâye bulamadım; video bunu olay olarak değil, çalışma mantığı olarak anlatıyor.",
    ],
    "sahneler": [
        {
            "slayt": {"tur": "baslik", "baslik": "Git", "alt": "Yapay zekâ çağında kayıt noktası"},
            "satirlar": [
                c("Dokuzuncu video: Git. Yapay zekâ hızlı çalışır; yanlış yaptığında da hızlı yapar. Bu yüzden projenin ilk işi, geri dönebileceğin bir kayıt noktasıdır."),
            ],
        },
        {
            "slayt": {
                "tur": "olay", "etiket": "Temmuz 2025 · Replit", "baslik": "Canlı veritabanı silindi",
                "maddeler": ["Kodu dondurma talimatı verilmişti", "Ajan: “geri alınamaz” dedi", "Sonradan veri geri getirildi"],
                "kaynak": "Kaynak: The Register, AI Incident Database",
            },
            "satirlar": [
                c("Temmuz 2025'te bir yapay zekâ ajanı, kodu dondurma talimatına rağmen bir şirketin canlı veritabanını sildi.", goster=1),
                c("Ajan geri almanın imkânsız olduğunu söyledi; yanlıştı, veri geri getirildi. Ders: bu tür iddiayı kendin kontrol et.", goster=3),
            ],
        },
        {
            "slayt": {
                "tur": "olay", "etiket": "3 Ekim 2026 · Cursor", "baslik": "Silme komutu yanlış yazıldı",
                "maddeler": ["Kaynak kod gitti", "Git klasörü gitti", "Elle alınan yedek de gitti: hepsi aynı diskteydi", "Geri Dönüşüm Kutusu'na düşmedi"],
                "kaynak": "Kaynak: Cursor forumu, kullanıcının kendi anlatımı",
            },
            "satirlar": [
                c("Ekim 2026'da bir geliştirici forumda anlattı: Cursor'un ajanı, klasör silme komutunu yanlış yazdı.", goster=1),
                c("Kaynak kod, Git klasörü ve elle aldığı yedek aynı diskteydi; üçü birden gitti.", goster=4),
                c("Yani Git tek başına yetmez: kayıt noktasının bir kopyası, ajanın ulaşamayacağı yerde olmalı.", goster=4),
            ],
        },
        {
            "slayt": {
                "tur": "olay", "etiket": "Git nedir?", "baslik": "Projenin zaman makinesi",
                "maddeler": ["Her kayıt noktasına “commit” denir", "Bozulursa son iyi noktaya dönersin", "Kaydetmediğin şeyi geri getiremez"],
                "kaynak": "",
            },
            "satirlar": [
                c("Git, projenin zaman makinesidir. Her kayıt noktasına commit denir; bozulursa son iyi noktaya dönersin. Ama yalnızca kaydettiğin şeyi geri getirir.", goster=3),
            ],
        },
        {
            "slayt": {
                "tur": "liste", "baslik": "Beş kural",
                "maddeler": [
                    "Göreve başlamadan önce kayıt al",
                    "Kaydı başka yere de gönder (GitHub gibi)",
                    "Silme komutunu sen oku",
                    "Parola ve anahtar Git'e girmez",
                    "Bozulunca önce dur",
                ],
            },
            "satirlar": [
                c("Birinci kural: göreve başlamadan önce kayıt al. Yapay zekâya yaz: bu klasörde Git başlat ve ilk kayıt noktasını al.", vurgu=0),
                c("İkinci kural: kaydı GitHub gibi uzak bir depoya da gönder. Disk gitse bile proje durur.", vurgu=1),
                c("Üçüncü kural: silme ve sıfırlama komutlarını yapay zekâ ancak senin onayınla çalıştırsın.", vurgu=2),
            ],
        },
        {
            "slayt": {
                "tur": "komut", "baslik": "Bunlardan birini görürsen dur",
                "komutlar": ["rm -rf", "rmdir /s /q", "git reset --hard", "git clean -fd"],
                "alt": "Hedef yolu kendin oku. Yanlış yazılmış bir yol, tüm diski silebilir.",
            },
            "satirlar": [
                c("Ekrandaki komutlardan birini görürsen dur ve hedef yolu kendin oku."),
            ],
        },
        {
            "slayt": {
                "tur": "liste", "baslik": "Beş kural",
                "maddeler": [
                    "Göreve başlamadan önce kayıt al",
                    "Kaydı başka yere de gönder (GitHub gibi)",
                    "Silme komutunu sen oku",
                    "Parola ve anahtar Git'e girmez",
                    "Bozulunca önce dur",
                ],
            },
            "satirlar": [
                c("Dördüncü kural: parola ve anahtar Git'e girmez. GitGuardian'ın 2026 raporuna göre, yapay zekâ destekli commit'lerde sızıntı ortalamanın yaklaşık iki katı. Sızan anahtarı silmek yetmez; değiştirmen gerekir.", vurgu=3),
                c("Beşinci kural: bozulunca yapay zekâyı durdur ve o diske yazma; son kayıt noktasına ve uzak depoya bak.", vurgu=4),
            ],
        },
        {
            "slayt": {"tur": "kapanis", "ozet": "Kayıt al · Uzağa gönder · Silme komutunu oku · Anahtarı sakla", "sonraki": "Ne yapacağına göre doğru yol"},
            "satirlar": [
                c("Özet: kayıt al, uzağa gönder, silme komutunu oku, anahtarı sakla. Sıradaki video: ne yapacağına göre doğru yol."),
            ],
        },
    ],
}

V10 = {
    "no": 10,
    "dosya": "10_Projeye_gore_yol_haritasi",
    "baslik": "Ne yapacağına göre doğru yol",
    "renk": "#22c55e",
    "sonraki": "Web sitesi yapıyorsan yasal zorunluluklar",
    "kaynaklar": [],
    "notlar": [
        "Bu videodaki dil ve araç eşleşmeleri yaygın, yerleşik seçimlerdir; sürüm numarası verilmedi. Yayın öncesi resmî belgeden doğrulanmalı (videoda da söyleniyor).",
        "Bu video için henüz ayrıca web araştırması yapılmadı; üretilmeden önce 'en yaygın yığın' ifadeleri güncel kaynakla (ör. yıllık geliştirici anketleri) desteklenebilir.",
    ],
    "sahneler": [
        {"slayt": None, "satirlar": [
            c("Onuncu video: ne yapacağına göre doğru yol. Yapay zekâya “hangi dille yapayım” diye sormadan önce üç şeyi söylemelisin: ne yapıyorsun, kim kullanacak, nerede çalışacak."),
            c("Web sitesi ya da web uygulaması: HTML, CSS ve JavaScript ya da TypeScript. Üstüne React, Vue ya da Svelte gibi bir çerçeve; sunucu için Node ya da Python."),
            c("Küçük bir tanıtım sitesi için çerçeveye gerek yok. Düz HTML ve CSS yeter; daha az parça, daha az hata."),
            c("Mobil uygulama: iPhone için Swift, Android için Kotlin. İkisini tek kodla istersen Flutter ya da React Native."),
            c("Masaüstü uygulama: Windows için C# ve .NET; her sistemde çalışsın istersen Electron ya da Tauri."),
            c("Ama önce şunu sor: bu iş bir web uygulamasıyla çözülmüyor mu? Çoğu zaman çözülür ve bakımı çok daha kolaydır."),
            c("Oyun: Unity C# ile, Unreal C++ ve Blueprint ile, Godot GDScript ile yazılır. Roblox'ta dil Luau."),
            c("Seçerken üç kural. Bir: yaygın olanı seç. Yapay zekâ, çok örneği olan teknolojide çok daha iyi çalışır."),
            c("İki: tek yığın kullan. Bir projede iki dil ve iki çerçeve, hata sayısını katlar."),
            c("Üç: sürümü yazdır ve resmî belgeden doğrulat. Yapay zekânın bilgisi eskiyebilir."),
            c("Her dilin standart araçları vardır: biçimlendirici, hata denetçisi ve test aracı. İlk günden kurdur; kalite buradan başlar."),
            c("Kararı karar defterine yaz: neden bu dil, neden bu çerçeve. Altı ay sonra kimse hatırlamaz."),
            c("İstek örneği: şunu yapacağım. Üç yığın öner. Artısını, eksisini ve bu projeye uyumunu yaz. Resmî belgeden doğrula."),
            c("Sıradaki video: web sitesi yapıyorsan yasal zorunluluklar."),
        ]},
    ],
}

V11 = {
    "no": 11,
    "dosya": "11_Web_sitesi_yasal_zorunluluklar",
    "baslik": "Web sitesi yapıyorsan: yasal zorunluluklar",
    "renk": "#ef4444",
    "sonraki": "Mobil uygulama ve oyunlarda mağaza kuralları",
    "kaynaklar": [
        ("KVKK 2026 idari para cezası tutarları (Cott Group)", "https://www.cottgroup.com/tr/mevzuat/item/yeniden-degerleme-oranina-gore-2026-yili-kvkk-idari-para-cezalari"),
        ("KVKK 2026 idari para cezaları (Mondaq)", "https://www.mondaq.com/turkey/data-protection/1726256/2026-y%C4%B1l%C4%B1-kvkk-%C4%B0dari-para-cezalar%C4%B1-g%C3%BCncel-tutarlar-ve-uyar%C4%B1lar"),
        ("KVKK çerez rehberi güncellemesi (Erdem & Erdem)", "https://www.erdem-erdem.av.tr/bilgi-bankasi/kisisel-verileri-koruma-kurumu-cerez-uygulamalari-hakkinda-rehberi-guncelledi"),
        ("E-ticaret siteleri hukuki yükümlülükler 2026 (FFK Partner)", "https://www.ffkpartnerhukuk.com.tr/e-ticaret-sitelerinin-hukuki-yukumlulukleri-2026-guncel-rehber/"),
        ("İYS kayıt yükümlülüğü (Moroğlu Arseven)", "https://www.morogluarseven.com/insights/publications/articles-en/guide-on-commercial-electronic-communication-management-system/"),
        ("CNIL: Google 325 M€, Shein 150 M€ (Privacy Laws & Business)", "https://www.privacylaws.com/news/cnil-fines-google-325-million-and-shein-150-million/"),
        ("İspanya, yetersiz gizlilik metni cezası (MLex)", "https://www.mlex.com/mlex/articles/2248536/unnamed-website-owner-pays-gdpr-fine-over-deficient-privacy-policy"),
    ],
    "notlar": [
        "Önemli: 'Yapay zekâyla yapılan siteye ceza kesildi' diye belgelenmiş bir yaptırım bulamadım. Bulduğum örneklerde ceza eksik/yetersiz gizlilik metnine kesiliyor; sitenin hangi araçla yapıldığı konu değil. Video bu yüzden 'araç fark etmez, sorumlu site sahibi' diyor.",
        "KVKK ceza bandı (85.437 – 1.709.200 TL) ikincil kaynaklardan (hukuk büroları); dayanak olarak gösterilen yeniden değerleme oranı %25,49 (Resmî Gazete 27.11.2025, sayı 33090). Resmî kaynaktan teyit edilmeli.",
        "KVKK çerez rehberi 2025'te güncellenmiş (videoya girmedi; eski 2022 yazılarına güvenme). Rehber tavsiye niteliğinde; 'eşit görünür düğmeler' ve 'devam etmek rıza değildir' ilkeleri ikincil kaynaklardan. Rehberin 2025 güncellemesi metni doğrudan okunamadı.",
        "ETBİS ve İYS ayrıntıları hukuk bürosu yazılarından; ETBİS tebliğinin yürürlük tarihi kaynaklar arasında 1 ve 11 Ağustos 2017 diye ayrışıyor (videoda tarih yok).",
        "GDPR tavanı (20 milyon € ya da %4) kanun metninden bilinen üst sınır; ceza bunun altında verilir. İspanya örneği MLex haberinden; resmî karar metni okunmadı.",
        "Bu video hukuki danışmanlık değildir; videonun sonunda da söyleniyor. Yayından önce bir hukukçu onaylamalı.",
    ],
    "sahneler": [
        {
            "slayt": {"tur": "baslik", "baslik": "Yasal zorunluluklar", "alt": "Web sitesi yapıyorsan"},
            "satirlar": [
                c("On birinci video: yasal zorunluluklar. Yapay zekâ siteyi bir saatte yapar; yasal metinleri çoğu zaman sen istemedikçe düşünmez."),
            ],
        },
        {
            "slayt": {"tur": "olay", "etiket": "Önce bunu bil", "baslik": "Araç fark etmez, sorumlu sensin",
                      "maddeler": ["Siteyi yapay zekâ yapmış olması cezayı değiştirmez", "Sorumlu: site sahibi", "Örneklerde ceza, eksik metne kesiliyor"],
                      "kaynak": ""},
            "satirlar": [
                c("Önce şunu bil: siteyi yapay zekânın yapmış olması cezayı değiştirmez; sorumlu site sahibidir. Örneklerde ceza, eksik metne kesiliyor.", goster=3),
            ],
        },
        {
            "slayt": {
                "tur": "liste", "baslik": "Türkiye'de ne gerekir?",
                "maddeler": [
                    "Aydınlatma metni (KVKK m.10)",
                    "Çerez: zorunlu olmayanlar için önce açık rıza",
                    "Düğmeler eşit görünür: Kabul · Reddet · Tercihler",
                    "Satış varsa: mesafeli satış sözleşmesi, cayma, iade",
                    "Kendi alan adından satış: ETBİS kaydı",
                    "Reklam e-postası / SMS: onay + İYS",
                ],
            },
            "satirlar": [
                c("Türkiye'de ilk kural: kişisel veri topladığın her yerde aydınlatma metni; kim topluyor, ne amaçla, kime aktarılıyor, kullanıcının hakları ne.", vurgu=0),
            ],
        },
        {
            "slayt": {
                "tur": "olay", "etiket": "Türkiye · 2026", "baslik": "Aydınlatma yükümlülüğüne aykırılık",
                "maddeler": ["85.437 – 1.709.200 TL", "Tutar her yıl yeniden değerleme oranıyla artıyor"],
                "kaynak": "Kaynak: hukuk büroları derlemeleri (Cott Group, Mondaq); resmî kaynaktan teyit et",
            },
            "satirlar": [
                c("Eksik bırakmanın 2026 cezası, kaynaklara göre 85.437 ile 1.709.200 lira arasında; her yıl yeniden değerleme oranıyla artıyor.",
                  ses="Eksik bırakmanın 2026 cezası, kaynaklara göre yaklaşık seksen beş bin ile bir milyon yedi yüz dokuz bin lira arasında; her yıl yeniden değerleme oranıyla artıyor.", goster=2),
            ],
        },
        {
            "slayt": {
                "tur": "liste", "baslik": "Türkiye'de ne gerekir?",
                "maddeler": [
                    "Aydınlatma metni (KVKK m.10)",
                    "Çerez: zorunlu olmayanlar için önce açık rıza",
                    "Düğmeler eşit görünür: Kabul · Reddet · Tercihler",
                    "Satış varsa: mesafeli satış sözleşmesi, cayma, iade",
                    "Kendi alan adından satış: ETBİS kaydı",
                    "Reklam e-postası / SMS: onay + İYS",
                ],
            },
            "satirlar": [
                c("İkinci kural: çerezler. Zorunlu olmayan çerezlerde, yani analitik ve reklamda, çerez yerleşmeden önce açık rıza gerekir.", vurgu=1),
                c("Kabul, reddet ve tercihler düğmeleri eşit görünmeli. “Siteyi kullanmaya devam ederek kabul etmiş sayılırsınız” rıza değildir.", vurgu=2),
                c("Üçüncü kural: para alıyorsan, mesafeli satış sözleşmesi, ön bilgilendirme, cayma ve iade koşulları sitede yazılı olmalı.", vurgu=3),
                c("Kendi alan adından satış yapıyorsan ETBİS kaydı gerekir. Reklam e-postası ya da SMS göndereceksen önce onay al ve İYS'ye kayıt ol.", vurgu=[4, 5]),
            ],
        },
        {
            "slayt": {
                "tur": "olay", "etiket": "Avrupa'dan ziyaretçin varsa", "baslik": "GDPR",
                "maddeler": ["Tavan: 20 milyon € ya da yıllık cironun %4'ü", "2025, Fransa: Shein 150 milyon €, Google 325 milyon € (çerezler)", "İspanya: online mağaza, yetersiz gizlilik metni, 6.000 €"],
                "kaynak": "Kaynak: Privacy Laws & Business, MLex",
            },
            "satirlar": [
                c("Avrupa'dan ziyaretçin varsa GDPR devreye girer: tavan ceza yirmi milyon avro ya da yıllık cironun yüzde dördü.", goster=1),
                c("2025'te Fransa'nın veri koruma kurumu, çerezler yüzünden Shein'e 150 milyon, Google'a 325 milyon avro kesti.", goster=2),
                c("Küçük siteler de kurtulmadı: İspanya'da bir online mağaza, yetersiz gizlilik metni yüzünden 6.000 avro ödedi.", goster=3),
            ],
        },
        {
            "slayt": {
                "tur": "istek", "baslik": "Yapay zekâya şunu yaz",
                "metin": "Bu site hangi kişisel verileri topluyor? Türkiye ve Avrupa için hangi yasal metinler gerekir? Her biri için resmî kaynağı göster ve bugünün tarihini yaz.",
            },
            "satirlar": [
                c("Yapay zekâya yaz: bu site hangi kişisel verileri topluyor? Türkiye ve Avrupa için hangi yasal metinler gerekir? Resmî kaynağı göster."),
                c("Metinleri yapay zekâ taslak olarak yazar; son hâlini bir hukukçu onaylamalı. Bu video bilgilendirme amaçlıdır, hukuki danışmanlık değildir."),
            ],
        },
        {
            "slayt": {"tur": "kapanis", "ozet": "Aydınlatma · Çerez · Satış metinleri · GDPR · Hukukçu onayı", "sonraki": "Mobil uygulama ve oyunlarda mağaza kuralları"},
            "satirlar": [
                c("Sıradaki video: mobil uygulama ve oyunlarda mağaza kuralları."),
            ],
        },
    ],
}

V12 = {
    "no": 12,
    "dosya": "12_Magaza_ve_platform_kurallari",
    "baslik": "Mobil ve oyun: mağaza ve platform kuralları",
    "renk": "#3b82f6",
    "sonraki": "Yapay zekânın en çok unuttuğu güvenlik ve kalite işleri",
    "kaynaklar": [
        ("Google Play: hesap silme ve veri güvenliği formu (Hunton, Help Net Security)", "https://www.helpnetsecurity.com/?p=259913"),
        ("Google Play kapalı test şartı (Google Play Console Yardım)", "https://support.google.com/googleplay/android-developer/answer/14151465"),
        ("Android hedef API şartı (Android Developers)", "https://developer.android.com/google/play/requirements/target-sdk"),
        ("Apple: uygulama içi hesap silme (App Store Review Guidelines 5.1.1(v))", "https://developer.apple.com/app-store/review/guidelines/#5.1.1"),
        ("Steam AI bildirimi (Valve ocak 2026, ikincil kaynaklar)", "https://www.prismnews.com/hobbies/video-games/valve-clarifies-steam-ai-disclosure-rules-internal-tools-exempt-content-disclosed"),
        ("Steamworks uygulama ücreti", "https://partner.steamgames.com/doc/gettingstarted/appfee"),
        ("Roblox yayın şartları (Creator Docs)", "https://create.roblox.com/docs/production/publishing/kids-and-select"),
    ],
    "notlar": [
        "Google'ın 'API 36' şartı: arama sonuçları 31 Ağustos 2026 tarihli şartı gösteriyor; eski yazılar API 35 diyor. Yayın öncesi resmî sayfadan doğrula.",
        "12 test kullanıcısı / 14 gün şartı: yalnızca 13 Kasım 2023 sonrası açılan KİŞİSEL hesaplar için; kurumsal hesapların muaf olduğu bilgisi üçüncü taraf kaynaklarda, resmî sayfada teyit edilmedi.",
        "Steam: video 'kod asistanları bildirilmez' diyor; bu bilgi ikincil haber kaynaklarından (Valve'in ocak 2026 güncellemesi). Resmî Steamworks sayfası açılamadı.",
        "Roblox yayın şartları 2026'da birkaç kez değişti (mayıs/haziran uygulamaları); TANDEM için yayından önce Creator Docs kontrol edilmeli. Güncel durum doğrulanmadı.",
    ],
    "sahneler": [
        {"slayt": None, "satirlar": [
            c("On ikinci video: mağaza ve platform kuralları. Uygulamanın ya da oyunun çalışması yetmez; mağaza onaylamalı. Kurallar sık değişir, buradaki bilgileri yayından önce resmî sayfadan doğrula."),
            c("Apple: kullanıcı hesap açabiliyorsa, uygulamanın içinden hesabı silme seçeneği şart. Hesabı yalnızca dondurmak yetmez."),
            c("Apple ile giriş sunuyorsan, hesap silinirken Apple'ın erişim anahtarını da iptal etmelisin."),
            c("Google Play: gizlilik politikası zorunlu. Veri güvenliği formu da zorunlu; eksikse uygulama yayınlanmaz ya da güncellenemez."),
            c("Google da hesap silmeyi ister: uygulamanın içinde ve web'de bulunabilir olmalı. Verinin kendisi de silinmeli."),
            c("31 Ağustos 2026'dan beri yeni uygulama ve güncellemeler Android 16'yı, yani API 36'yı hedeflemeli."),
            c("2023 Kasım'ından sonra açılan kişisel Google hesaplarında, yayından önce on iki test kullanıcısıyla on dört gün kapalı test şartı var."),
            c("Steam: oyun başına yüz dolar ücret. Yapay zekâ içeriği varsa bildirmek gerekir: oyunda görünen ya da oyun sırasında üretilen içerik. Kaynaklara göre kod yazmak için kullandığın araçlar bildirilmez."),
            c("Roblox, TANDEM'in platformu. 2026'da yaş doğrulaması sıkılaştı: sohbet için yaş kontrolü; tüm yaşlara açık yayın için kimlik doğrulama, iki adımlı doğrulama, abonelik ve oyun incelemesi."),
            c("Her deneyim için yaş anketini doldurmazsan, on üç yaş altına gösterilmez. Güncel şartları Creator Docs sayfasından kontrol et."),
            c("Çocuklara yönelik her şeyde kurallar daha sıkı: yaş derecesi, veri toplama, reklam. Çocuk kullanıcı ihtimali varsa baştan planla."),
            c("İstek örneği: bu uygulamayı Apple, Google ve Steam'e yüklemeden önce kontrol listesi çıkar. Her madde için resmî sayfanın bağlantısını ve bugünün tarihini yaz."),
            c("Sıradaki video: yapay zekânın en çok unuttuğu güvenlik ve kalite işleri."),
        ]},
    ],
}

V13 = {
    "no": 13,
    "dosya": "13_Guvenlik_ve_kalite_unutulanlar",
    "baslik": "Yapay zekânın en çok unuttuğu güvenlik ve kalite işleri",
    "renk": "#a855f7",
    "sonraki": "Yayından önce tek komutla denetim",
    "kaynaklar": [
        ("Veracode 2026 raporu özeti (Let's Data Science)", "https://letsdatascience.com/news/veracode-finds-ai-code-security-stalled-at-56-616847d8"),
        ("Lovable / Supabase RLS, CVE-2025-48757", "https://blog.vibecoder.me/post-mortem-lovable-cve-2025-48757"),
        ("16.000+ Supabase veritabanı açık (Cybernews)", "https://cybernews.com/news/16000-supabase-databases-exposed/"),
        ("Uydurma paket / slopsquatting (SD Times)", "https://sdtimes.com/coding-assistants/hallucinated-code-real-threat-how-slopsquatting-targets-ai-assisted-development/"),
        ("OWASP Top 10:2025", "https://owasp.org/Top10/2025/"),
        ("Avrupa Erişilebilirlik Yasası (Avrupa Komisyonu erişilebilirlik merkezi)", "https://accessible-eu-centre.ec.europa.eu/content-corner/news/eaa-comes-effect-june-2025-are-you-ready-2025-01-31_en"),
    ],
    "notlar": [
        "Veracode: 2026 raporunda güvenlik testi geçme oranı ortalama %56 (2025'te ~%45 açıklı). Raporun istemlerinde güvenlik talimatı yoktu; bu yüzden videoda 'sen istemezsen çoğu zaman düşünmez' deniyor, 'her kod %44 açıklı' denmiyor. Birincil rapor okunmadı.",
        "Lovable/Supabase: 170+ uygulama (CVE-2025-48757) ve UpGuard'ın 16.326 veritabanı bulgusu satıcı/haber kaynaklarından; sayılar kaynaklar arasında değişiyor.",
        "Uydurma paket: USENIX 2025 çalışması (örneklerin ~%20'si olmayan paket, %43'ü tekrarlıyor) ikincil özetten; birincil makale okunmadı.",
        "Erişilebilirlik muafiyeti (10 çalışan altı, 2 milyon € altı) hizmet sağlayıcı mikro işletmeler için; kaynaklar bu ayrımı net yazmıyor, video 'kendi durumunu doğrulat' diyor. Ceza tutarları ülkeye göre; rakam verilmedi.",
    ],
    "sahneler": [
        {"slayt": None, "satirlar": [
            c("On üçüncü video: yapay zekânın en çok unuttuğu işler. Veracode'un Temmuz 2026 raporuna göre, yapay zekâ kodunun güvenlik testini geçme oranı ortalama yüzde elli altı. Sözdizimi neredeyse kusursuz; güvenlik değil."),
            c("Rapordaki istemlerde güvenlik talimatı yoktu. Yani güvenliği sen istemezsen, çoğu zaman o da düşünmez."),
            c("Bir: yetki. Lovable ve Supabase ile yapılan uygulamalarda satır düzeyinde yetki kapalı geliyordu; 2025'te yüz yetmişten fazla uygulama açıkta kaldı."),
            c("2026'da UpGuard, herkese açık tabloları olan 16.326 Supabase veritabanı saptadı; yarısından fazlasında kişisel veri belirtisi vardı."),
            c("Test: kendi anahtarınla başka bir kullanıcının verisini okuyabiliyor musun? Okuyabiliyorsan açık var."),
            c("İki: uydurma paket. Bir araştırmada yapay zekâ örneklerinin yaklaşık yüzde yirmisi, var olmayan bir paket adı önerdi; uydurmaların yüzde kırk üçü her seferinde tekrarlandı."),
            c("Saldırgan o adla bir paket yayınlayıp bekler. Önerilen paketi kurmadan önce bak: kim yayınlamış, kaç indirmesi var, resmî mi?"),
            c("OWASP'ın 2025 listesinde ilk üç sırada yetki, yanlış yapılandırma ve yazılım tedarik zinciri var. Gizli anahtarları dokuzuncu videoda konuştuk."),
            c("Dört: erişilebilirlik. Avrupa Erişilebilirlik Yasası 28 Haziran 2025'ten beri uygulanıyor. Avrupa'daki kullanıcıya hizmet veren web siteleri, mobil uygulamalar ve e-ticaret kapsamda."),
            c("Teknik ölçüt EN 301 549, yani WCAG 2.1 AA seviyesi. Yapay zekâya klavyeyle kullanımı, renk karşıtlığını ve resim açıklamalarını kontrol ettir."),
            c("Küçük hizmet sağlayıcılar için muafiyet var ama dar. Kendi durumunu doğrulat."),
            c("Beş: yedek ve test. Yapay zekâya test yazdır ve çalıştırt. Yedeği de geri yükleyerek dene; denenmemiş yedek, yedek değil varsayımdır."),
            c("İstek örneği: bu projeyi bir saldırgan gibi incele. Her bulgu için dosyayı, satırı ve düzeltmeyi yaz. Emin olmadıklarını işaretle."),
            c("Sıradaki video: yayından önce tek komutla denetim."),
        ]},
    ],
}

V14 = {
    "no": 14,
    "dosya": "14_Yayindan_once_denetim",
    "baslik": "Yayından önce denetim",
    "renk": "#14b8a6",
    "sonraki": "",
    "kaynaklar": [],
    "notlar": [
        "Bu video 09-13'ün özetidir; yeni olgu içermiyor, o yüzden ayrıca kaynak yok. Kontrol listesindeki her madde önceki videolardaki bir bulguya bağlı.",
    ],
    "sahneler": [
        {"slayt": None, "satirlar": [
            c("Son video: yayından önce denetim. Yapay zekâ ekibin en hızlı üyesi. Unuttuklarını ise bir listeyle yakalarsın."),
            c("Yayın kapısında on soru var. Bir: Git'te son kayıt ve uzak depoda bir kopya var mı?"),
            c("İki: kodda parola ya da anahtar kalmış mı? Üç: yetki testini yaptım mı?"),
            c("Dört: kişisel veri topluyor muyum? Aydınlatma, gizlilik ve çerez metinleri hazır mı? Beş: kullanıcılarım hangi ülkelerde?"),
            c("Altı: çocuk kullanıcı olabilir mi? O zaman kurallar sıkılaşır. Yedi: mağaza ya da platform formları, hesap silme ve yaş derecesi tamam mı?"),
            c("Sekiz: bağımlılıklar gerçek, güncel ve lisansı uygun mu? Dokuz: erişilebilirlik temel kontrolleri yapıldı mı?"),
            c("On: yedeği geri yüklemeyi denedim mi? Hata izleme ve geri dönüş planı var mı?"),
            c("Bunların hepsini tek komutla yapay zekâya denetlet. Proje türünü ve kullanıcı ülkelerini yaz."),
            c("Çıktı bir tablo olsun: bulgu, kanıt, risk, düzeltme. Kanıt; dosya ve satır ya da resmî kaynak bağlantısı olsun."),
            c("Doğrulayamadığı her şeye “doğrulanmadı” yazsın. Tahmini, kesin gibi sunmasın."),
            c("Sonra bulguları sen dene. Hukuki metinleri bir hukukçu onaylasın; yayın kararı proje sahibinin."),
            c("Yayından sonra da bitmiyor: ceza tutarları her yıl güncelleniyor, mağaza kuralları sık değişiyor. Yılda iki kez yeniden denetle."),
            c("Özet: kayıt al, yolu seç, yasal metinleri koy, mağaza kurallarını oku, güvenliği ölç, yayından önce denetle. Başarılar!"),
        ]},
    ],
}

VIDEOLAR = [V09, V10, V11, V12, V13, V14]
