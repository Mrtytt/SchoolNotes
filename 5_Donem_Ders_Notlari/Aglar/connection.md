### Kullanıcının Internete Bağlanma Süreci: Adım Adım

### **1. Başlangıç: Kullanıcının Ağa Bağlanması**
- **Senaryo**: Kullanıcı internete bağlanıyor, örneğin bir dizüstü bilgisayar veya mobil cihaz.
- **DHCP Kullanımı**:
  - Ağa katılan cihazın bir IP adresine, ilk-hop yönlendiricinin adresine ve DNS sunucusunun adresine ihtiyacı var.
  - DHCP (Dynamic Host Configuration Protocol) kullanılarak bu bilgiler alınır.
  - DHCP istemcisi olan cihaz, bir DHCP isteği (request) gönderir. Bu istek:
    - **UDP** içinde kapsüllenir, ardından **IP**, sonra **Ethernet** çerçevesine eklenir ve yayılır.
    - Yönlendirici bu isteği alır, çözer ve DHCP ACK cevabıyla gerekli bilgileri sağlar.

### **2. ARP (Adres Çözümleme Protokolü)**
- **DNS Sorgusundan Önce**: IP adresi üzerinden iletişim kurmak için cihazın yönlendiricinin MAC adresini bilmesi gerekir.
- **Süreç**:
  - ARP sorgusu yayınlanır.
  - Yönlendirici ARP cevabı ile MAC adresini döner.
  - Artık cihaz DNS sorgusunu göndermek için yönlendiricinin MAC adresine sahiptir.

### **3. DNS Kullanımı**
- **Amaç**: Kullanıcı bir web sayfasını (örneğin, `www.google.com`) ziyaret etmek istiyor. Bunun için IP adresi gerekir.
- **Süreç**:
  - DNS sorgusu UDP, IP ve Ethernet protokolleri kullanılarak DNS sunucusuna gönderilir.
  - DNS sunucusu, `www.google.com`’un IP adresini içeren bir cevap döner.


### **4. TCP Bağlantısının Kurulması**
- **HTTP İstekleri İçin**: Kullanıcı web sitesine erişmek için TCP bağlantısı kurmalıdır.
- **Adımlar**:
  - TCP'nin 3-yönlü el sıkışma (3-way handshake) süreci başlar:
    1. Cihaz TCP SYN segmenti gönderir.
    2. Sunucu TCP SYNACK ile yanıt verir.
    3. Cihaz ACK ile yanıt verir.
  - Bağlantı kurulmuş olur.

### **5. HTTP İstek ve Cevapları**
- **Web Sitesinin Gönderimi**:
  - HTTP isteği TCP soketi üzerinden gönderilir.
  - Sunucu, HTTP yanıtı ile birlikte istenen web sayfasını döner.
  - Web sayfası tarayıcıda görüntülenir.

### **Özet**
Bu süreç, ağ katmanlarının (Link, IP, UDP/TCP, ve HTTP) bir arada çalışmasıyla gerçekleşir. Her adımda farklı bir protokol görev alır. Şunlara dikkat et:
- DHCP: IP adresi ve ağ ayarları için.
- ARP: MAC adreslerini çözmek için.
- DNS: Alan adlarını IP adresine dönüştürmek için.
- TCP: Veri aktarımı için güvenilir bir bağlantı sağlamak için.
- HTTP: Web içeriğini almak için.


