### Önemli Başlıklar - Detaylandırılmış Açıklamalar

#### 1. **SDN (Software Defined Networking)**
##### Bilimsel Açıklama:
SDN, geleneksel ağ yönetiminin karmaşıklığını azaltmak için geliştirilmiş bir ağ mimarisidir. Geleneksel ağlarda veri iletimi (data plane) ve yönlendirme (control plane) bir arada çalışır. Örneğin, bir yönlendirici (router), veriyi iletirken aynı zamanda hangi yolu izleyeceğine karar verir. SDN'de ise bu iki fonksiyon ayrıştırılmıştır:  
1. **Control Plane (Yönetim Katmanı):** Ağın yönlendirme mantığını ve politikalarını belirler. Bu, genellikle yazılım tabanlı bir denetleyici tarafından kontrol edilir.
2. **Data Plane (Veri Katmanı):** Veriyi fiziksel olarak ileten ağ cihazlarıdır. Yönlendirme kararlarını almaz, sadece iletimi yapar.  
Bu ayrım sayesinde:
- Ağ kolayca programlanabilir ve dinamik olarak kontrol edilebilir.
- Trafik akışları optimize edilebilir.
- Yeni hizmetler hızlıca uygulanabilir.
##### Ek Örnek:
Bir şirket ağına yeni bir güvenlik politikası eklemek için tüm cihazları tek tek yapılandırmak yerine, SDN kontrol katmanında yapılan bir değişiklik tüm ağa yansıtılabilir.  

#### 2. **SNMP/MIB (Simple Network Management Protocol / Management Information Base)**
##### Bilimsel Açıklama:
**SNMP**, ağ cihazlarının durumunu izlemek ve yönetmek için kullanılan bir protokoldür.  
**MIB** ise bu cihazlardan toplanan verilerin düzenlendiği bir bilgi tabanıdır.  
**SNMP’nin çalışma prensipleri:**
1. **Agent:** Ağ cihazlarında çalışan SNMP modülü, cihazın durum bilgilerini toplar ve MIB’de saklar.
2. **Manager:** Ağ yöneticisi, SNMP komutlarını göndererek bu verilere erişir veya cihazı yapılandırır.  
**SNMP İşlemleri:**
- **GET:** Cihazdan veri talep eder (ör. CPU kullanımı, bağlantı durumu).  
- **SET:** Cihaza yapılandırma komutları gönderir (ör. IP değiştirme).  
- **TRAP:** Cihaz bir problem algıladığında yöneticiyi bilgilendirir (ör. bir bağlantının kopması).  
##### Ek Örnek:
Bir ağ yöneticisi, bir yönlendiricinin performansını kontrol etmek istediğinde SNMP kullanarak CPU kullanımı veya trafik istatistiklerini alabilir. Eğer cihaz bir sorun algılarsa (örneğin bir port kapanmışsa), SNMP TRAP mesajıyla yöneticiyi uyarır.  

#### 3. **NETCONF/YANG**
##### Bilimsel Açıklama:
- **NETCONF (Network Configuration Protocol):** Ağ cihazlarının yapılandırılması, izlenmesi ve yönetimi için kullanılan bir protokoldür. NETCONF, XML tabanlıdır ve ağ cihazlarına uzaktan erişim sağlar. Geleneksel yöntemlere göre daha otomatik ve güvenlidir.
- **YANG (Yet Another Next Generation):** Ağ cihazlarının yapılandırma ve izleme süreçlerinde kullanılan veri modellerini tanımlayan bir dildir.  
**NETCONF Özellikleri:**
- Yapılandırma ve durumu okuma.
- Güvenli uzaktan erişim.
- Hataları kolayca algılama ve düzeltme.  
**YANG’ın Avantajları:**
- Standart bir dil olarak her tür ağ cihazında aynı yapılandırma şeması kullanılabilir.
- Karmaşık ağ topolojilerinde düzen sağlar.  
##### Ek Örnek:
Bir ağ yöneticisi, YANG modellerini kullanarak bir veri merkezi ağı için yapılandırma kuralları oluşturabilir. NETCONF ile bu kuralları uzaktaki yönlendirici ve anahtarlara (switch) uygulayabilir.  

#### 4. **Subnet Mask**
##### Bilimsel Açıklama:
Subnet mask, IP adreslerini mantıksal olarak iki bölüme ayırır:
1. **Ağ Bölümü (Network Part):** IP adresinin hangi ağta olduğunu gösterir.  
2. **Cihaz Bölümü (Host Part):** Ağdaki cihazları tanımlar.  
Örneğin:  
IP adresi: `192.168.1.10`  
Subnet mask: `255.255.255.0`  
- İlk üç oktet (`192.168.1`) ağ adresini, son oktet (`10`) ise cihaz adresini temsil eder.  
- Bu sayede ağ trafiği bölünerek yönetilir ve daha verimli bir iletişim sağlanır.  
##### Ek Örnek:
Bir şirketin iki ofisi vardır:  
- Ofis A: 192.168.1.0/24  
- Ofis B: 192.168.2.0/24  
Subnet mask ile hangi cihazın hangi ofiste olduğu belirlenir. Ofisler arasında iletişim gerekiyorsa, yönlendirme işlemi yapılır.  

#### 5. **Default Gateway**
##### Bilimsel Açıklama:
Default gateway, bir ağdaki cihazların başka bir ağa veri göndermesini sağlayan bir yönlendiricidir. Örneğin:
- Eğer veri aynı ağta bir cihaza gönderilecekse, doğrudan iletilir.
- Eğer veri farklı bir ağa gitmesi gerekiyorsa, önce default gateway üzerinden geçer.  
**Çalışma Prensibi:**  
1. Cihaz, hedef IP adresini kontrol eder.  
2. Eğer hedef IP, cihazın kendi ağı dışındaysa, veri default gateway’e yönlendirilir.  
3. Default gateway, veriyi hedef ağa ulaştırır.  
##### Ek Örnek:
Bir evdeki bilgisayar (IP: 192.168.1.5) internete bağlanmak istediğinde, önce yönlendiriciye (default gateway, örn: 192.168.1.1) veri gönderir. Yönlendirici, bu veriyi internet servis sağlayıcısına (ISP) iletir.  

#### 6. **DHCP (Dynamic Host Configuration Protocol)**
##### Bilimsel Açıklama:
DHCP, bir ağdaki cihazlara otomatik olarak IP adresi, subnet mask ve default gateway bilgilerini atayan bir protokoldür.  
**Çalışma Adımları:**
1. **DISCOVER:** Cihaz ağa bağlandığında bir DHCP sunucusu arar.
2. **OFFER:** DHCP sunucusu cihaz için bir IP adresi önerir.
3. **REQUEST:** Cihaz, önerilen adresi talep eder.
4. **ACK:** DHCP sunucusu adresi onaylar ve cihaz artık ağta iletişim kurabilir.  
##### Ek Örnek:
Bir otelde herkesin bir oda numarası olduğunu düşünün. Yeni gelen bir misafire resepsiyon (DHCP sunucusu) boş bir oda numarası verir ve misafir artık bu odada kalabilir.  

#### 7. **SWITCH / SELF LEARNING**
##### Bilimsel Açıklama:
**Switch**, bir ağdaki cihazlar arasında veri paketlerini ileten bir cihazdır.  
**Self-learning** özelliği, switch’in bağlı cihazların MAC adreslerini öğrenmesini ve tabloya kaydetmesini sağlar.  
**Çalışma Prensibi:**
1. Bir cihazdan gelen ilk veri paketi, switch tarafından tüm portlara iletilir (broadcast).  
2. Switch, gelen paketin kaynak MAC adresini kaydeder ve cihazın hangi porta bağlı olduğunu öğrenir.
3. Gelecek veri paketlerinde switch, veriyi doğru porta iletir.  
##### Ek Örnek:
Bir postacı düşünün. İlk başta adresleri bilmez ve tüm mektupları rastgele dolaştırır. Ancak zamanla hangi adresin nerede olduğunu öğrenir ve doğrudan doğru kişiye teslim yapar.

