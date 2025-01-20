### Bilgisayar Ağları Hafta 11-12 – Klasik Sınav Soruları ve Çözümleri

#### Soru 1: Geleneksel routing algoritmaları ile SDN kontrol düzlemi arasındaki farkları açıklayın.
**Cevap:**
- Geleneksel routing algoritmalarında kontrol düzlemi dağıtık şekilde her routerda bulunur. SDN’de ise kontrol düzlemi merkezi bir SDN kontrolcüsü tarafından yönetilir.
- Geleneksel yöntemlerde routerlar, birbirleriyle bilgi alışverişi yaparak routing tablolarını hesaplar. SDN’de routing tablosu SDN kontrolcüsü tarafından hesaplanır ve routerlara iletilir.
- SDN, yazılımla tanımlı bir mimari sunduğu için esneklik ve yeniliklere daha açıktır.

#### Soru 2: Dijkstra algoritmasını tanımlayın ve algoritmanın temel adımlarını örnek bir grafik üzerinde uygulayarak gösterin.
**Cevap:**Dijkstra algoritması, bir kaynaktan tüm diğer düğülere olan en kısa yolları hesaplar.
- **Adımlar**:
    - Kaynak düğümün maliyetini 0, diğerlerini sonsuz olarak başlatın.
    - Kaynak düğümü “ziyaret edildi” olarak işaretlenir.
    - Komşu düğümlerle olan maliyetler güncellenir.
    - En düşük maliyetli düğüm seçilir ve ziyaret edilir.
    - Tüm düğümler ziyaret edilene kadar devam edilir.
- **Örnek**:
    - **Grafik**:
    - A -> B: 1, A -> C: 4, B -> C: 2, B -> D: 6, C -> D: 3
    - **Adımlar**:
        - A’dan başla: (A=0, B=1, C=4, D=sonsuz)
        - B ziyaret edildi: (A=0, B=1, C=3, D=7)
        - C ziyaret edildi: (A=0, B=1, C=3, D=6)
        - D ziyaret edildi: (A=0, B=1, C=3, D=6)

#### Soru 3: Bellman-Ford algoritmasının temel farkını Dijkstra algoritması ile karşılaştırın ve avantajlarını/dezavantajlarını belirtin.
**Cevap:**
- Dijkstra, sadece pozitif ağırlıklı kenarlar için çalışrken, Bellman-Ford negatif ağırlıklı kenarları destekler.
- Bellman-Ford daha yavaş bir algoritmadır (O(VE)), Dijkstra ise O(V^2) zaman karmaşıklığına sahiptir (heap kullanımıyla O(VlogV)).
- Bellman-Ford, negatif ağırlıklı döngüleri algılayabilir.

#### Soru 4: Yazılım Tanımlı Ağın (SDN) avantajlarını ağ yönetimi açısından tartışın.
**Cevap:**
- **Kolay yönetim:** Merkezi kontrol sayesinde tüm ağ daha kolay yönetilir.
- **Yenilik:** Yeni protokollerı ve uygulamaları hızlıca test etme ve uygulama imkânı sunar.
- **Trafik optimizasyonu:** Trafiğin etkin bir şekilde yeniden yönlendirilmesini sağlar.

#### Soru 5: Geleneksel ağ kontrol mekanizmalarındaki tıkanıklıkların SDN ile nasıl aşıldığını açıklayın.
**Cevap:**
- Geleneksel yapılarda router’ların bireysel olarak karar vermesi, tıkanıklıklara neden olabilir.
- SDN, trafik akışını merkezi olarak analiz eder ve tıkanıklıkları önlemek için önceden önlemler alabilir.

#### Soru 6: OSPF protokolünün temel çalışma prensiplerini açıklayın.
**Cevap:**
- OSPF (Open Shortest Path First), link-state tabanlı bir yönlendirme protokolüdür.
- Routerlar ağ topolojisini tespit eder ve Dijkstra algoritmasıyla en kısa yolları hesaplar.
- Link-state reklamları, tüm ağda yayılır ve tüm routerların aynı topoloji bilgisini paylaşması sağlanır.

#### Soru 7: BGP protokolünde AS-PATH ve NEXT-HOP kavramlarını açıklayın ve bunların rolünü tartışın.
**Cevap:**
- **AS-PATH:** Routing tablosunda bir hedefe ulaşırken geçilmesi gereken Autonomous System (AS) dizisidir. Daha kısa AS-PATH, genellikle tercih edilir.
- **NEXT-HOP:** Bir sonraki hedef routerı ifade eder. Routerlar paketleri NEXT-HOP routerına iletir.

#### Soru 8: Intra-AS ve Inter-AS routing arasındaki farkları açıklayın.
**Cevap:**
- **Intra-AS:** Aynı AS içindeki routerlar arasında yönlendirme (OSPF gibi).
- **Inter-AS:** Farklı AS’ler arasında yönlendirme (BGP gibi).
- İntra-AS yönlendirmede performans önemliyken, Inter-AS yönlendirmede politikalar daha önemlidir.

#### Soru 9: Hot potato routing nedir? Örnekle açıklayın.
**Cevap:**
- Routerların, bir paketi ağa en düşük maliyetle çıkarmaya çalışmasıdır. Örneğin, bir router en yakın NEXT-HOP’a paketleri iletir.

#### Soru 10: BGP’nin politik tabanlı routing yapısının avantajları ve dezavantajları nelerdir?
**Cevap:**
- **Avantajlar:** Trafiği kontrol etme, önceliklendirme ve güvenlik.
- **Dezavantajlar:** Yüksek karmaşıklık, hız kaybı ve yanlış politikaların etkisi.

#### Soru 11: SNMP protokolünün temel mesaj türlerini (Örneğin GetRequest, Trap) açıklayın.
**Cevap:**
- **GetRequest:** Veri talebi.
- **Trap:** Cihaz tarafından gönderilen beklenmedik olay bildirimleri.

#### Soru 12: NETCONF’un özelliklerini ve YANG veri modelleme dilini tanımlayın.
**Cevap:**
- **NETCONF** XML tabanlı bir protokoldür. Cihaz konfigürasyonlarını uzak bir yöneticiye aktarır.
- **YANG** NETCONF’ta kullanılan veri modelleme dilidir ve konfigürasyon doğruluğunu sağlar.

#### Soru 13: Bir ağda SNMP ve NETCONF kullanarak cihaza erişim örneklerini karşılaştırın.
**Cevap:**
- **SNMP:** Daha basit ama sınırlı yönetim yetenekleri.
- **NETCONF:** Daha karmaşık ama detaylı yönetim imkânı sunar.

#### Soru 14 : YANG ile bir ağ cihazı için XML tabanlı bir konfigürasyon örneği yazın.
**Cevap:**
<config>
  <interface>
    <name>Ethernet0/0</name>
    <mtu>1500</mtu>
  </interface>
</config>

#### Soru 15 : SNMP’deki Management Information Base (MIB) yapısını ve önemi tartışın.
**Cevap:**
- **MIB** cihazlardan veri alınması ve izlenmesi için bir veri yapısıdır.

#### Soru 16 : ICMP protokolünün temel amacını ve kullanım alanlarını açıklayın.
**Cevap:**
- Hata raporlama ve durum bildirimleri.
- Ping, traceroute gibi test aracı olarak kullanılır.

#### Soru 17 : Ping ve traceroute gibi ICMP tabanlı araçların nasıl çalıştığını detaylıca açıklayın.
**Cevap:**
- **Ping:** Echo Request ve Echo Reply mesajlarıyla ulaşılabilirlik kontrolü yapar.
- **Traceroute:** TTL değerini arttırarak ara routerları belirler.

#### Soru 18 : ICMP mesaj türlerinden “Destination Unreachable” ve “Time Exceeded” mesajlarının ne anlama geldiğini örnekler ile gösterin.
**Cevap:**
- **Destination Unreachable:** Hedefe ulaşılamıyor (network veya port sorunları).
- **Time Exceeded:** Paketlerin TTL değeri sıfıra ulaştı.

#### Soru 19 : Bir ağda tıkanıklık (congestion) durumunda ICMP’nin rolünü açıklayın.
**Cevap:**
- ICMP, kaynak cihaza tıkanıklığı bildiren “Source Quench” mesajları gönderebilir.

#### Soru 20 : ICMP protokolünün güvenlik zafiyetleri ve bunlara karşı alınabilecek önlemleri tartışın.
**Cevap**
- **Zafiyetler:** ICMP flood, Ping of Death gibi siber saldırılar.
- **Önlemler:** ICMP mesajlarının filtrelenmesi ve aşırı kullanımın izlenmesi.
