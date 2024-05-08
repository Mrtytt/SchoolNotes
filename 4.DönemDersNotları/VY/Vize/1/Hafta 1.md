
## Donanım ve Yazılım

- Donanım : Somut parçaların tamamıdır.
- Yazılım : Donanımların çalışmasını sağlayan programların tamamı.
- Program : Komutlar topluluğu, bu komutların işi gerçekleştirme işlemi.
- Her bir program yazılıma ait bir elemandır.

## Bilgisayar Mimarisi

- Donanım - Mikro Kod - Çevirici Dil Programı - Çekirdek - İşletim Sistemi ve Uygulamaları

## İşletim Sistemleri

- Bilgisayarda çalışan, bilgisayar donanım kaynaklarını yöneten ve çeşitli uygulama yazılımları için yaygın servisleri sağlayan bir yazılımlar bütünüdür.
- Her yerde vardır.
- İşlevselliklerini donanımı programlayabilme niteliklerinden alırlar.

## Algroitma

- Giriş(Veri) -> Algoritma -> Çıkış(Sonuç)

- Problemi çözmek veya amaca ulşamak için yapılan işlemlere algoritma denir.

- Birden fazla algoritma ile çözülebilir.

### Algoritma Türleri

- Yinelemeli Algoritmalar
- Özyinelemeli (Böl & Yönet) Algoritmalar
- Rastgele Algoritmalar
- Açgözlü(Greedy) Algoritmalar
- Dinamik Programlama
- Yaklaşma Algoritmaları
- Genetik Algoritmalar

## Veri Yapıları

- Algoritmalar tarafından işlenen en temel elemanlardır.
- int, string gibi olanlar **temel veri yapıları**
- struct, class gibi olanlar **tanımlamalı veri yapıları**

### Tanımlamalı Veri Yapıları

- Struct : Veri yapıları bir araya gelir.
- Union : En fazla yer işgal eden veri yapısının bouyutunda olur hepsi.
- Bit Düzeyinde Erişim.

## Veri Yapılarına Neden İhtiyaç Duyulur?

- Yazılımların programlanması ve yönetimi zorlaşmaktadır.

- Temiz kavramsal yapılar ve bu yapıları sunan çerçeve programları daha etkin ve daha doğru program yazmayı sağlar.

## Veri Modeli

- Problemin çözümü için kavramsal bir yaklaşımdır.
- En uygun ve en etkin.
- Çalışma hızı ve bellek gereksinimi hakkında bilgi verir.

### Liste ve Bağlantılı Liste Veri Modeli

#### Liste
- Dizi şeklinde sıralı veya sırasız.
- Ardışıl erişim.
- Dinamik yaklaşım.
- Arama -> O(n), Ekleme -> O(1), Silme Maliyeti -> O(1) veya O(n)
- Esnek bellek kullanımı.

#### Bağlantılı Liste

- Kendi değerleri ve bir sonraki elemanın adresleri tutulur.

- Bağlantı bilgisi bulunur.

### Ağaç Veri Modeli

- Hızlı erişim.
- Dinamik yaklaşım.
- Esnek bellek kullanımı.
- Tasarım esnekliği.

### Graph Veri Modeli

- Örneğin, bir şehrin trafik altyapısından en yüksek akışın sağlanması, taşıma şirketinin en verimli taşıma şekli

### Durum Makinası Veri Modeli

- Örneğin bir robot kolunun hareketi, şifre çözme, gerçek zamanlı işletim sistemlerinde proses kontrolü

![[veriModelleri.png]]