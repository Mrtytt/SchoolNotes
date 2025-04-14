# OpenGL ile Basit Şekil Çizimi ve Optimizasyon Önerileri

## Kodun Genel İşleyişi
Bu kod, OpenGL ve GLFW kullanarak ekranda sekiz adet üçgen çizen bir uygulama oluşturmaktadır. Uygulama aşağıdaki adımları takip eder:

1. **GLFW Kütüphanesini Başlatma**: OpenGL'in işlevlerini kullanabilmek için GLFW başlatılır ve pencere oluşturulur.
2. **GLAD ile OpenGL İşlevlerini Yükleme**: GLAD, OpenGL fonksiyonlarını yüklemek için kullanılır.
3. **Shader Programı Oluşturma**: OpenGL'in grafik işlemlerini gerçekleştirebilmesi için vertex ve fragment shader'ları oluşturulup bağlanır.
4. **Vertex Verilerini Hazırlama**: Üçgenleri oluşturmak için gerekli olan köşe verileri (vertices) tanımlanır ve OpenGL'e aktarılır.
5. **Render Döngüsü**: Sürekli olarak ekranda çizim işlemleri gerçekleştirilir ve kullanıcı girdileri işlenir.
6. **Kaynakları Serbest Bırakma**: Program sonlandığında bellekten gereksiz veriler temizlenir.

---

## Önemli Fonksiyonlar

### `void framebuffer_size_callback(GLFWwindow* window, int width, int height)`
Bu fonksiyon pencerenin boyutu değiştirildiğinde çağrılır ve OpenGL'in viewport'unu yeni pencere boyutlarına uyacak şekilde ayarlar.

### `void processInput(GLFWwindow* window)`
Kullanıcıdan gelen girdi olaylarını kontrol eder. `ESC` tuşuna basıldığında pencere kapanmasını sağlar.

### `int main()`
Ana fonksiyon, programın tüm temel bileşenlerini içerir:
- GLFW başlatma ve pencere oluşturma
- OpenGL fonksiyonlarını yükleme
- Shader programlarının oluşturulması ve kullanılması
- Üçgenlerin çizimi için gerekli olan vertex verilerini OpenGL'e aktarma
- Render döngüsü
- Kaynakların serbest bırakılması

---

## Optimizasyon Önerileri

### 1. **Shader Programı Önceden Derleyip Önbelleğe Alın**
Shader programlarının her çalıştırmada yeniden derlenmesi yerine, önceden derlenmiş ve doğrulanmış bir cache mekanizması kullanarak yükleme süresini azaltabilirsiniz.

### 2. **Tek Bir Draw Call Kullanımı**
Kod şu an `glDrawArrays(GL_TRIANGLES, 0, 24);` kullanarak çizim yapıyor. Eğer üçgenler tekrar eden bir yapıdaysa, `GL_ELEMENT_ARRAY_BUFFER` kullanarak **index buffer (EBO)** ile daha verimli bir çizim yapılabilir.

### 3. **VAO ve VBO Kullanımı**
Şu an her render döngüsünde VAO ve VBO bağlanıyor. Ancak, bunlar yalnızca bir kez tanımlanıp bağlanabilir ve döngü içinde tekrar bağlanmadan kullanılabilir.

### 4. **GLFW'nin `swapInterval(1)` Kullanımı**
GLFW'nin `glfwSwapInterval(1);` fonksiyonunu kullanarak **V-Sync** etkinleştirilerek GPU gereksiz yere fazla çalıştırılmaz ve yırtılma (tearing) önlenir.

### 5. **Vertex Shader'ı Optimizasyonu**
Vertex shader şu an yalnızca pozisyon verisini kullanıyor. Eğer renk veya normal gibi veriler kullanılmıyorsa, gereksiz değişkenler kaldırılarak shader daha hafif hale getirilebilir.

### 6. **Uniform Değişkenlerle Renk Değiştirme**
Renk değiştirme için her karede yeni bir shader derleyip yüklemek yerine, **uniform değişkenler** kullanarak daha verimli bir renk değişimi sağlanabilir.

---

Bu öneriler uygulanarak OpenGL programınızın hem performansı hem de taşınabilirliği artırılabilir.

