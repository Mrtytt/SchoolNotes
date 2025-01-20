**CRC (Cyclic Redundancy Check) Algoritması**

CRC (Cyclic Redundancy Check), bilgisayar ağları ve depolama cihazlarında veri aktarımı sırasında hataların tespit edilmesi için kullanılan bir algoritmadır. Temel olarak, gönderilen veri üzerine bir "kontrol kodu" eklenir ve alıcı, bu kodu doğrulayarak veri üzerinde bir hata olup olmadığını kontrol eder.

---

### **CRC Algoritmasının Çalışma Adımları**

#### **1. Veri ve Bölücü Polinomunun Tanımlanması**
- Gönderilecek veri bir ikili sayı (binary) dizisidir.
- Bir "bölücü polinom" seçilir. Bu polinomun ikili karşılığı, hata kontrol kodunun hesaplanmasında kullanılır.
- Örneğin:
  - **Veri**: `1101011011`
  - **Bölücü Polinom**: `1011` (Bu, genellikle sabit bir uzunlukta önceden tanımlanır.)

---

#### **2. Veriye Ekstra Bit Eklenmesi**
- Verinin sonuna, bölücü polinomun derecesi kadar sıfır eklenir. Bu ekleme, veri ile kontrol kodunun birlikte işlenmesini sağlar.
- Bölücü polinomun derecesi, en yüksek dereceli terim sayısıdır (bölücü `1011` için derece 3'tür).
- Örnek:
  - **Veri**: `1101011011`
  - **Eklenmiş Bitler**: `000` (3 bit)
  - **Yeni Veri**: `1101011011000`

---

#### **3. Mod 2 Bölmesi (XOR İşlemi)**
- Eklenmiş veri, bölücü polinoma göre "Mod 2 bölme" işlemi yapılır. Mod 2 bölme, normal bölme gibi çalışır ancak çıkarmalar yerine XOR işlemi kullanılır.
- Bölme işlemi, en soldaki bitlerden başlanarak yapılır ve kalan, her adımda güncellenir.
- Örnek:
  - İlk adımda, `1101` ile `1011` XOR yapılır:
    ```
    1101
    XOR
    1011
    ----
    0110
    ```
  - Kalan (`0110`), bir sonraki bit eklenerek işleme devam eder.

---

#### **4. CRC Kodunun Elde Edilmesi**
- Bölme tamamlandığında, kalan, veriyle birlikte gönderilecek CRC kodudur.
- Örneğin, yukarıdaki işlemin sonunda kalan `011` ise, bu CRC kodudur.

---

#### **5. Veri ve CRC'nin Gönderilmesi**
- Veri, CRC ile birleştirilerek alıcıya gönderilir:
  - **Gönderilen**: `1101011011` + `011` = `1101011011011`

---

#### **6. Alıcı Tarafındaki Doğrulama**
- Alıcı, gelen veriyi aynı bölücü polinomu kullanarak tekrar Mod 2 bölme işlemi yapar.
- Eğer kalan `0` ise, veri hatasızdır. Eğer kalan farklı bir değer içeriyorsa, hata tespit edilir.

---

### **Örnek**

**Gönderici Tarafı:**
- **Veri**: `1101011011`
- **Bölücü Polinom**: `1011`
- **Eklenmiş Veri**: `1101011011000`
- **Mod 2 bölmesi sonucu kalan**: `011`
- **Gönderilen Veri**: `1101011011` + `011` = `1101011011011`

**Alıcı Tarafı:**
- **Gelen Veri**: `1101011011011`
- **Mod 2 bölmesi yapıldığında kalan**: `0` (Hatasız veri)

---

### **Avantajlar**
- CRC, basit ve hızlı bir hata tespit yöntemi sunar.
- Özellikle iletişim protokollerinde yaygın olarak kullanılır (Ethernet, USB vb.).

### **Sınırlamalar**
- Hataları yalnızca tespit eder, düzeltemez.
- Çok küçük ihtimalle bazı hataları gözden kaçırabilir.

