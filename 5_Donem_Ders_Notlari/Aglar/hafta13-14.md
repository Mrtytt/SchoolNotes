### Bilgisayar Ağları Hafta 13-14 – Klasik Sınav Soruları ve Cevapları

#### Soru 1: Bağlantı katmanının temel görevlerini açıklayın.
**Cevap:** Bağlantı katmanı, iki fiziksel olarak bağlı cihaz arasında veri iletimi sağlar. Görevleri:
- Çerçeveleme (Framing): Veriyi çerçevelere bölerek iletir.
- Hata Tespiti ve Düzeltme: Veri iletimindeki hataları algılar ve düzeltir.
- Akış Kontrolü: Verici ve alıcı arasında uyum sağlar.
- MAC (Ortam Erişim Kontrolü): Paylaşılan ortamda kanal erişimini yönetir.

#### Soru 2: Framing (çerçeveleme) ve link erişimının ağ iletişimindeki rolünü tartışın.
**Cevap:** Framing, ağ veri paketlerini fiziksel ortamda taşımak üzere daha küçük parçalara ayırarak şekillendirir. Link erişim, paylaşılan bir ortamda (Ethernet veya Wi-Fi) hangi cihazın veri göndereceğine karar verir.

#### Soru 3: Hata tespiti ve düzeltme yöntemleri arasındaki farkları açıklayın.
**Cevap:**
- **Hata Tespiti:** Hata olduğunu belirler (parite kontrolü, CRC gibi yöntemlerle).
- **Hata Düzeltme:** Hataları düzeltir. Örneğin, ileri hata düzeltme (FEC) yöntemi.

#### Soru 4: CRC (Cyclic Redundancy Check) algoritmasının nasıl çalıştığını bir örnekle açıklayın.
**Cevap:** CRC, veriye belirli bir polinom bölmesi yaparak kalanı hesaplar. Alıcı, aynı bölme işlemini yaparak verinin hatasız olup olmadığını kontrol eder. Örneğin:
- Veri: 1101
- Polinom: 101
- Sonuç kalan: 10

#### Soru 5: Parite kontrolü (Parity Checking) yöntemlerini karşılaştırarak açıklayın.
**Cevap:**
- Tek Bit Paritesi: Veri içindeki 1 bit sayısının tek/çift olmasına göre ek bit ekler.
- Çift Boyutlu Parite: Satır ve sütun pariteleri ekleyerek daha fazla hata tespiti sağlar.

#### Soru 6: Ethernet çerçeve yapısını detaylandırarak, her bir alanın görevini açıklayın.
**Cevap:**
- **Preamble:** İletim sürerini senkronize eder.
- **Hedef ve Kaynak MAC Adresi:** Veriyi gönderen ve alıcı cihazları tanımlar.
- **Tip:** Taşınan üst katman protokolünü belirtir.
- **CRC:** Hata kontrolü sağlar.

#### Soru 7: CSMA/CD protokolünün çalışmasını bir örnekle anlatın.
**Cevap:**
1. Cihaz, kanalı dinler.
2. Kanal boşsa veri gönderir.
3. Çakışma algılanırsa çakışma sinyali gönderir ve geri çekilir.
4. Rastgele bir süre sonra yeniden dener.

#### Soru 8: MAC adreslerinin yapılandırılması ve kullanımı hakkında bilgi verin.
**Cevap:**
MAC adresleri, cihazın NIC (Ağ Kartı) ROM'una kayıtlıdır ve benzersizdir. Yerel iletim için kullanılır. IP adreslerinin aksine, taşınabilir.

#### Soru 9: ARP (Adres Çözümleme Protokolü) tablosunun işlevini açıklayın.
**Cevap:** ARP tablosu, IP adreslerini MAC adreslerine eşleştirir. Bu, cihazların aynı ağda doğru hedefe veri göndermesini sağlar.

#### Soru 10: Bir ağda iki farklı alt ağa paket yönlendirme sürecini örnek bir senaryoda açıklayın.
**Cevap:**
1. Cihaz, hedef IP adresini analiz eder.
2. Alt ağda değilse paketi birinci aşama router'a iletir.
3. Router, hedefe ulaşır.

#### Soru 11: VLAN’ların temel prensiplerini ve sağladığı avantajları açıklayın.
**Cevap:** VLAN, ağları mantıksal gruplara ayırır. Trafiği izole eder, güvenliği artırır ve verimliliği optimize eder.

#### Soru 12: Token Passing protokolünün nasıl çalıştığını bir örnekle açıklayın.
**Cevap:**
Token Passing, bir cihazdan diğerine geçen “token” iletimiyle kontrol edilir. Token’ı alan cihaz veri gönderir.

#### Soru 13: ALOHA ve Slotted ALOHA protokollerinin farklarını açıklayın.
**Cevap:**
- **ALOHA:** Herhangi bir zamanda iletim yapar, çakışma ihtimali yüksek.
- **Slotted ALOHA:** Sabit zaman aralıklarında iletim yapar, daha az çakışma.

#### Soru 14: Bağlantı katmanında yaygın olarak kullanılan hata tespit yöntemlerini karşılaştırın.
**Cevap:**
- **CRC:** Yüksek doğruluk.
- **Parity:** Daha basit ama sınırlı hata tespiti.

#### Soru 15: Bir Ethernet anahtarının (switch) kendini öğrenme sürecini detaylandırın.
**Cevap:** Anahtar, gelen paketlerin kaynak MAC adreslerini kayıt eder ve hedefe uygun porttan iletir.

#### Soru 16: MPLS (Çoklu Protokol Etiket Anahtarlama) teknolojisinin avantajlarını açıklayın.
**Cevap:** MPLS, hızlı veri iletimi, yük dengesi ve trafik yönetimi sağlar.

#### Soru 17: Bir web isteğinin tüm ağ katmanlarında nasıl işlediğini açıklayın.
**Cevap:**
1. Uygulama: HTTP isteği.
2. Taşıma: TCP bağlantısı.
3. Ağ: IP adresleme.
4. Bağlantı: Veri iletimi.

#### Soru 18: Yerel bir ağda IP adresinin MAC adresine nasıl çözüldüğünü adım adım açıklayın.
**Cevap:**
1. ARP isteği yayınlama.
2. Hedef cihaz, ARP cevabı gönderir.
3. MAC adresi ARP tablosuna eklenir.

#### Soru 19: Broadcast ve point-to-point bağlantılar arasındaki farkları açıklayın.
**Cevap:**
- **Broadcast:** Tüm cihazlara yayın.
- **Point-to-Point:** Tek bir cihazla iletişim.

#### Soru 20: Bir ağda trafiği izole etmek için VLAN’ların nasıl yapılandırılabileceğini tartışın.
**Cevap:** VLAN’lar port tabanlı veya MAC adresine göre yapılandırılır. Trafik izole edilir ve yönetim kolaylaşır.

