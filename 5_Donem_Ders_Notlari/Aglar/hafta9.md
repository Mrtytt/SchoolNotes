### Bilgisayar Ağları Hafta 13-14 - "Hücresel Haberleşme" Slaytı

#### Soru 1:
**Hücresel ağ standartları arasında modülasyon tekniklerinin farklılıkları nedir? Çeşitli modülasyon tekniklerinin ağ performansına etkileri nasıldır?**

**Cevap:**
Hücresel ağlar, farklı nesillerde farklı modülasyon tekniklerini benimsemiştir.

- **1G (Analog Sistemler):** Frekans Modülasyonu (FM) ve Faz Modülasyonu (PM) kullanır. Veri iletimi yerine yalnızca analog ses için optimize edilmiştir.
- **2G:** Dijital hale geçmiş ve GMSK (Gaussian Minimum Shift Keying) gibi daha verimli dijital modülasyon teknikleri kullanılmıştır. Bu, veri iletiminde görülen çok düşük hata oranlarına olanak sağlamıştır.
- **3G:** Geniş bant teknolojileriyle birlikte QPSK (Quadrature Phase Shift Keying) ve daha karmaşık modülasyonlar gelir. Yüksek bant genişliği ihtiyacı karşılanır.
- **4G:** 64-QAM gibi yüksek dereceli modülasyonlar öne çıkar. Bu, daha hızlı veri transferine olanak tanır ancak parazitlere karşı daha duyarlıdır.
- **5G:** Daha ileri bir adım olarak 256-QAM’i destekler. Bu, maksimum veri hızını önemli ölçüdé arttırır ancak güvenilirlik konusunda optimize edilmiş ağ çözümülerine ihtiyaç duyar.

Modülasyon teknikleri, ağ performansına özellikle veri hızı, bant genişliği verimliliği ve parazite dayanıklılık açısından çok büyük etki eder.

---

#### Soru 2:
**RRC protokol yığını (Protocol Stack) nedir ve hangi katmanları içerir? Bu protokol özellikle hücresel haberleşmede hangi problemlerin çözülmesine yardımcı olur?**

**Cevap:**
RRC (Radio Resource Control) protokolü, mobil cihaz ile çekirdek ağ arasındaki iletişim yönetiminden sorumludur ve protokol yığını şu katmanları içerir:

1. **Fiziksel Katman:** Veri çerçevelerini taşır.
2. **MAC (Medium Access Control):** Veri paketlerini önceliklendirir ve çakışmayı önler.
3. **RLC (Radio Link Control):** Hata kontrolü ve veri akışını sağlar.
4. **PDCP (Packet Data Convergence Protocol):** Şifreleme ve sıkıştırma gibi üst düzey fonksiyonları yerine getirir.

**Problemlere Çözüm:**
- **Bağlantı Yönetimi:** Bağlantıların kurulumu, sürdürülmesi ve sonlandırılması.
- **Elçetik (Handover):** Bir baz istasyonundan diğerine kesintisiz geçiş.
- **Kaynak Dağıtımı:** Radyo frekansını verimli kullanır.
- **Güvenlik:** Verilerin şifrelenmesi ve yetkisiz erişimlerin önlenmesi.

---

#### Soru 3:
**"Carrier Aggregation" (Taşıyıcı Birleştirme) nedir? Mobil şebekelerde hangi avantajları sunar?**

**Cevap:**
Carrier Aggregation (CA), birden fazla frekans bant genişliğinin tek bir veri akışında birleştirilmesi teknolojisidir. Özellikle 4G ve 5G ağlarında yaygın olarak kullanılır.

**Avantajları:**
1. **Yüksek Veri Hızı:** Farklı bantlardan gelen taşıyıcıları birleştirerek daha hızlı veri iletimi.
2. **Spektrum Verimliliği:** Kullanılmayan spektrum alanlarının verimli kullanımı.
3. **Görüşme Kalitesi:** Daha az parazit ve kesintisiz bir deneyim.

---

#### Soru 4:
**Self Organizing Networks (SON) teknolojisinin temel işlevleri nelerdir ve şebeke operatörlerine ne gibi faydalar sağlar?**

**Cevap:**
SON, mobil şebekelerin otomatize edilmesi için kullanılan bir teknolojidir. Üç ana işlevi bulunur:

1. **Kendini Optimizasyon:** Trafiğin dinamik olarak dengelenmesi ve enerji tasarrufu.
2. **Kendini Yapılandırma:** Yeni baz istasyonların otomatik kurulumu.
3. **Kendini Onarma:** Arızaların ve kesintilerin otomatik tespiti ve giderilmesi.

**Faydaları:**
- Maliyetlerin azaltılması (insan müdahalesinin azalması).
- Daha az kesinti ve daha iyi kapsama alanı.
- Gerçek zamanlı sorun giderme.

---

#### Soru 5:
**5G’nin sunduğu ana hizmetler nelerdir ve bu hizmetlerin özellikleri nelerdir?**

**Cevap:**
5G, üç ana hizmet sunar:

1. **eMBB (Enhanced Mobile Broadband):** Çok hızlı veri iletimi (>10 Gbps), daha fazla bant genişliği ve HD medya deneyimi sunar.
2. **URLLC (Ultra-Reliable Low-Latency Communication):** 1 ms’den az gecikme süresiyle kritik uygulamalarda (otonom araçlar, tıbbi robotlar) kullanılır.
3. **mMTC (Massive Machine-Type Communication):** Çok sayıda IoT cihazını destekler. Enerji verimliliği ve uzun batarya ömrü sunar.

Bu hizmetler, mobil ağların özellikle IoT, sanal gerçeklik (VR) ve endüstriyel otomasyon gibi alanlarda yaygın şekilde kullanılmasını sağlar.

