### Bilgisayar Ağları Hafta 7-8 – Klasik Sınav Soruları ve Cevapları

#### 1. Ağ katmanının iki temel işlevini tanımlayın ve her biri için örnek verin.
**Cevap:**
- **Yönlendirme:** Paketlerin kaynak ile hedef arasındaki yolu belirler. Örneğin, bir IP paketi hedef ağa yönlendirilir.
- **İletim:** Bir router’ın giriş portundan çıkış portuna paketleri taşır. Örneğin, bir paketin belirli bir çıkış portuna iletilmesi.

#### 2. Veri düzlemi ve kontrol düzlemi işlevselliklerini karşılaştırın.
**Cevap:**
- **Veri düzlemi:** Yerel router bazında kararlar alır, paketleri giriş portundan çıkış portuna iletir.
- **Kontrol düzlemi:** Ağ genelinde yönlendirme tabloları oluşturur ve paketlerin hangi yolları izleyeceğini belirler.

#### 3. Bir router’ın temel bileşenlerini ve bunların rolleri nedir?
**Cevap:**
- **Giriş portları:** Gelen paketlerin alındığı yer.
- **Anahtarlama kumaşı:** Paketlerin doğru çıkış portuna iletilmesini sağlar.
- **Çıkış portları:** Paketlerin ağın sonraki düğümünü hedeflediği yerdir.

#### 4. Giriş portu kuyruklama ile çıkış portu kuyruklama arasındaki fark nedir?
**Cevap:**
- Giriş portu kuyruklama, anahtarlama kumaşı yavaş olduğunda paketlerin girişte bekletilmesidir.
- Çıkış portu kuyruklama, paketlerin çıkışta link hızından daha hızlı gelmesinden kaynaklanır.

#### 5. Head-of-Line (HOL) blokajı nedir ve ağ performansını nasıl etkiler?
**Cevap:**
- HOL blokajı, bir kuyruğun başındaki paketin bloklanması nedeniyle arkadaki paketlerin de işlenememesi durumudur. Bu, bant genişliğinin düşmesine neden olabilir.

#### 6. Hedef tabanlı iletimi açıklayın.
**Cevap:**
- Paketlerin sadece hedef IP adresine göre yönlendirildiği geleneksel iletim yöntemidir.

#### 7. En uzun önek eşleştirmenin amacı nedir ve adım adım bir örnek verin.
**Cevap:**
- Amaç, bir paketin hedef IP adresine en uygun yönlendirme tablosu girdisini bulmaktır.
- Örnek: Hedef IP: 192.168.1.10
  - Tabloda şu önekler var: 192.168.0.0/16, 192.168.1.0/24
  - En uzun önek: 192.168.1.0/24.

#### 8. CIDR nedir ve sınıf tabanlı adreslemeden farkı nedir?
**Cevap:**
- CIDR, adres alanlarının önceden belirlenmiş sınıflar yerine rastgele uzunluklarda bölünmesine izin verir. Bu, adres alanını daha verimli kullanır.

#### 9. DHCP protokolünün amacı nedir? DHCP istemci-sunucu iletişim sürecini açıklayın.
**Cevap:**
- DHCP, istemcilerin dinamik olarak IP adresi alabilmesini sağlar.
- Aşamalar:
  - **Keşif:** İstemci sunucuyu yayın yoluyla bulur.
  - **Teklif:** Sunucu, istemciye bir IP adresi sunar.
  - **Talep:** İstemci, teklif edilen adresi kabul eder.
  - **Onaylama:** Sunucu, adresi onaylar ve ağ bilgilerini sağlar.

#### 10. Bir alt ağ nedir ve alt ağ maskeleri nasıl kullanılır?
**Cevap:**
    - Alt ağ, bir IP ağının bölümü olup, cihazların birbiriyle router kullanmadan iletişim kurabilmesini sağlar.
    - Alt ağ maskesi, IP adresinin ağ ve host kısımlarını ayırmak için kullanılır.

#### 11. NAT’ın nasıl çalıştığını ve faydalarını açıklayın.
**Cevap:**
    - NAT, yerel ağ cihazlarının bir ortak IP adresi paylaşmasını sağlar. Gelen ve giden paketlerin IP adreslerini yeniden yazar.
    - Faydalar: Adres tasarrufu, gizlilik ve ISP’den bağımsızlık.

#### 12. IPv4 ve IPv6 adresleme formatları arasındaki temel farklar nelerdir?
**Cevap:**

    - IPv4: 32 bit, noktalı ondalık yazım (192.168.0.1).
    - IPv6: 128 bit, sekizli bloklar halinde yazım (2001:db8::1).

#### 13. IPv4'ten IPv6'ya geçişin zorluklarını tartışın ve tünelleme kavramını açıklayın.
**Cevap:**
    - Zorluklar: Tüm cihazların aynı anda geçememesi, karmaşık uyumluluk.
    - Tünelleme: IPv6 paketlerinin IPv4 paketlerine sarılarak taşınması.

#### 14. FCFS, Öncelik Zamanlaması ve Ağırlıklı Adil Kuyruklama (WFQ) yöntemlerini karşılaştırın.
**Cevap:**

    - **FCFS:** Gelen sıraya göre iletim.
    - **Öncelik Zamanlaması:** Öncelikli paketler önce iletilir.
    - **WFQ:** Her sınıfa ağırlık verilir, bant genişliği adil şekilde paylaşılır.

#### 15. Tampon yönetiminin önemini ve paket kaybını nasıl önlediğini açıklayın.
**Cevap:**
    - Tamponlar, paketlerin aşırı yük durumunda depolanmasını sağlar. Bu, ağın paket kaybı yaşamaması için kritik bir işlevdir.

#### 16. Bir ağ tarafından sağlanabilecek üç QoS garantisini listeleyin ve açıklayın.
**Cevap:**
    - **Garantili Teslim:** Paketlerin hedefe ulaşması garantilenir.
    - **Minimum Bant Genişliği:** Bir akışa belirli bir bant genişliği ayrılır.
    - **Gecikme Sınırı:** Paketlerin gecikmesi bir sınırda tutulur.

#### 17. "Best-effort" hizmeti ile garantili QoS arasındaki farkları açıklayın.
**Cevap:**
    - **Best-effort:** Hiçbir garanti verilmez.
    - **Garantili QoS:** Teslimat, bant genişliği ve gecikme garantileri sunulur.

#### 18. Genelleştirilmiş iletimde "eşleştirme + işlem" soyutlaması nedir? Bir örnek verin.
**Cevap:**
    - Gelen paketin başlığı eşleştirilir ve buna uygun bir işlem (iletme, düzenleme, silme) uygulanır.
    - Örnek: Kaynak IP = 10.0.0.1 ise paketi çıkış porta ilet.

#### 19. OpenFlow'un SDN’deki rolünü ve ağ programlanabilirliğine etkisini açıklayın.
**Cevap:**
    - OpenFlow, ağları kontrol düzleminden programlamaya izin verir. Bu, dinamik ve esnek ağ yönetimini mümkün kılar.

#### 20. Middlebox nedir ve geleneksel router'lardan nasıl farklılık gösterir? Modern ağlardaki işlevlerine örnek verin.
**Cevap:**
    - Middlebox, veri paketlerini filtrelemek, önbellekleme yapmak veya güvenlik sağlamak gibi router’lardan farklı şekilde çalışan cihazlardır.
    - Örnek: NAT, güvenlik duvarları, yük dengeleyiciler.
