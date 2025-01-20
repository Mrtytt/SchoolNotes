## Önemli Notlar

### 1. INTRA-AS (Intra-Autonomous System)
#### Ne Demek?
Intra-AS, tek bir otonom sistem içinde yapılan yönlendirmeyi ifade eder. Örneğin, bir firmanın veya bir üniversitenin kendi iç ağı.
#### Bilimsel Açıklama:
- **Otonom Sistem Nedir?**:
  Bir organizasyona ait ağların bir araya gelerek oluşturduğu sistemdir.
- **Intra-AS Protokolleri:**
  - **RIP (Routing Information Protocol):** Küçük ağlar için uygundur, hop sayısını temel alır.
  - **OSPF:** Link-state protokolüdür, büyük ağlar için uygundur.
  - **EIGRP (Enhanced Interior Gateway Routing Protocol):** Cisco’ya özel, karmaşık bir protokol.
#### Önemli Bilgiler:
- Intra-AS yönlendirme, otonom sistem içinde optimum yolları bulmaya odaklanır.
- Bu protokoller genelde daha hızlıdır ve daha az karmaşıktır.

### 2. OSPF (Open Shortest Path First)
#### Ne Demek?
OSPF, bilgisayar ağlarında kullanılan bir yönlendirme protokolüdür. Ağda veri paketlerinin en kısa yoldan hedefe ulaşmasını sağlar. Bir tür "trafik polisi" gibi çalışır ve ağdaki tüm yolları öğrenip en uygun rotayı belirler.
#### Bilimsel Açıklama:
- **Protokol Türü:** Link-State Routing Protocol
- **Çalışma Mantığı:** 
  1. Her yönlendirici (router) bağlı olduğu ağların bir haritasını çıkarır.
  2. Bu bilgiler tüm yönlendiricilere gönderilir (LSA - Link State Advertisement).
  3. Dijkstra algoritması kullanılarak en kısa yol hesaplanır.
- **Bölgeler (Areas):** 
  - Area 0 (Backbone Area): Diğer tüm alanların bağlı olduğu ana bölge.
  - Bölgesel yönlendirme ile ölçeklenebilirlik artırılır.
- **Avantajları:** Döngüden kaçınma, hızlı ağ değişikliklerine adaptasyon, geniş ölçekli ağlar için uygunluk.
- **Kullanım Alanları:** Büyük kurumsal ağlar, servis sağlayıcı ağları.
#### Ezberlenmesi Gereken Detaylar:
- OSPF'nin Dijkstra algoritmasını kullandığını unutma.
- Her yönlendirici ağdaki tüm bağlantıları bilir; buna **Link State Database (LSDB)** denir.
- OSPF, TCP yerine **IP protokolü üzerinde çalışır**.

### 3. INTER-AS (Inter-Autonomous System)
#### Ne Demek?
Inter-AS, farklı otonom sistemler arasındaki yönlendirmeyi ifade eder. İnternet üzerindeki iletişim bu protokol sayesinde sağlanır.
#### Bilimsel Açıklama:
- **Kullanılan Protokol:** Border Gateway Protocol (BGP).
- **Çalışma Mantığı:**
  - BGP, bir Path Vector protokolüdür. Hangi yolların kullanılacağını, politikalar ve maliyetler belirler.
  - Hedefe giden yollar hakkında bilgi paylaşılır.
- **Avantajı:** Büyük ölçekli yönlendirmeyi mümkün kılar.
- **Örnek:** Bir internet servis sağlayıcısının başka bir servis sağlayıcıyla iletişim kurması.
#### Detaylar:
- İnter-AS yönlendirme, global ölçekte ağları bağlar.
- **Default Route (Varsayılan Yönlendirme):** BGP, default route kullanarak veri paketlerini iletebilir.

### 4. BGP (Border Gateway Protocol)
#### Ne Demek?
BGP, otonom sistemler arasında en iyi yönlendirme yollarını belirler. İnternetin "omurgası" olarak kabul edilir.
#### Bilimsel Açıklama:
- **Çalışma Prensibi:**
  - Her AS (Otonom Sistem), kendi politikalarını belirler.
  - Rotalar belirlenirken "AS Path", "Next Hop", ve "Local Preference" gibi parametreler dikkate alınır.
- **İç ve Dış BGP:** 
  - **iBGP:** Aynı AS içindeki iletişim.
  - **eBGP:** Farklı AS’ler arasındaki iletişim.
- **Özellikleri:**
  - Döngü önleme için AS Path kullanır.
  - Politika tabanlı yönlendirme yapabilir.
#### Önemli Noktalar:
- İnternetin global yönlendirme protokolüdür.
- AS numaraları (örneğin, AS64512) ile çalışır.

### 5. CRC (Cyclic Redundancy Check)
#### Ne Demek?
CRC, veri iletiminde hataları tespit etmek için kullanılan bir yöntemdir. Verinin doğru iletildiğinden emin olmak için bir kontrol kodu oluşturur.
#### Bilimsel Açıklama:
- **Nasıl Çalışır?**
  1. Gönderici, veri için bir CRC kodu hesaplar ve bunu veriyle birlikte yollar.
  2. Alıcı, aynı işlemi tekrar yaparak gönderilen kodla karşılaştırır.
  3. Kodlar farklıysa hata oluşmuş demektir.
- **Kullanılan Alanlar:**
  - Ethernet çerçeveleri.
  - Dosya aktarımı.
  - Depolama cihazları (örneğin, sabit diskler).
#### Önemli Detaylar:
- CRC, sadece hatayı tespit eder, düzeltmez.
- **Polinomlar:** CRC hesaplamasında kullanılan matematiksel ifadeler.

### 6. Ethernet
#### Ne Demek?
Ethernet, cihazların bir yerel ağ (LAN) içinde iletişim kurmasını sağlayan teknolojidir. Okulda öğrencilerin aynı bahçede oyun oynamasına benzer.
#### Bilimsel Açıklama:
- **Standart:** IEEE 802.3.
- **Çalışma Prensibi:** Veriler çerçeveler (frames) olarak iletilir.
- **Protokoller:**
  - CSMA/CD (Çarpışma Algılama): Çarpışmaları önler.
- **Hızlar:** 10 Mbps’den 100 Gbps’ye kadar değişir.

### 7. CSMA/CD (Carrier Sense Multiple Access with Collision Detection)
#### Ne Demek?
Ağ üzerindeki cihazlar sırayla veri gönderir. Çarpışma olursa iletim durdurulur ve tekrar denenir.
#### Bilimsel Açıklama:
1. Cihazlar ortamın boş olduğunu kontrol eder.
2. Ortam boşsa veri gönderilir.
3. Çarpışma olursa cihazlar rastgele bir süre bekler ve tekrar gönderir.
#### Önemli Detaylar:
- Ethernet ağlarında kullanılır.
- Modern ağlarda CSMA/CD yerine anahtarlar (switch) kullanılır.

### 8. ARP (Address Resolution Protocol)
#### Ne Demek?
ARP, bir IP adresini fiziksel (MAC) adrese çevirmek için kullanılır.
#### Bilimsel Açıklama:
- **Çalışma Prensibi:** 
  1. Yayın (broadcast) sorgusu yapılır.
  2. Hedef cihaz MAC adresini yanıt olarak gönderir.
- **Kullanım Alanı:** IPv4 ağları.

### 9. MAC (Media Access Control)
#### Ne Demek?
MAC adresi, bir cihazın fiziksel adresidir. Bu adres, cihazların birbirini tanımasını sağlar.
#### Bilimsel Açıklama:
- **Format:** 48-bit (örneğin, 00:1A:2B:3C:4D:5E).
- **Kullanım Alanı:** Ethernet, Wi-Fi.

### 10. VLAN (Virtual Local Area Network)
#### Ne Demek?
VLAN, fiziksel ağları sanal olarak bölümlere ayırır.
#### Bilimsel Açıklama:
- **Standart:** IEEE 802.1Q.
- **Avantajları:** Yayını sınırlandırır, güvenliği artırır.

### 11. ALOHA ve Slotted ALOHA
#### Ne Demek?
- **ALOHA:** Herkes istediği zaman veri gönderir.
- **Slotted ALOHA:** Veriler zaman dilimlerine bölünür.
#### Bilimsel Açıklama:
- **ALOHA:** Çarpışma oranı yüksektir.
- **Slotted ALOHA:** Çarpışma oranı daha düşüktür.
