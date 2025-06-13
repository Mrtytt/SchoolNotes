### 1. Projenin Amacı ve Kapsamı
Bu projenin temel amacı, günümüzde oyun dünyasında ve grafik teknolojilerinde sıkça kullanılan Ray Tracing yani ışın izleme yönteminin, DirectX 12 ile nasıl uygulandığını detaylı bir şekilde incelemekti. Microsoft’un DirectX 12 API’si ile birlikte gelen bu teknoloji, grafiklerde fiziksel gerçekçiliği oldukça ileri bir seviyeye taşıyor. 

Bu kapsamda, öncelikle DirectX 12’nin grafik programlamadaki yeri üzerinde durduk. Ardından, Ray Tracing’in geleneksel rasterization yöntemlerinden hangi yönlerle ayrıldığını ele aldık. Bununla birlikte, DirectX Ray Tracing yani DXR teknolojisinin yapısını oluşturan temel bileşenleri inceleyerek, ışığın sahne içinde nasıl izlendiğini ve sahnedeki objelerle nasıl etkileşim kurduğunu anlamaya çalıştık.
## -------------------------------------------------------------

### 2. Proje Adımları
Projemizi daha etkili bir şekilde yürütebilmek için süreci birkaç adıma böldük. İlk adımımız araştırma ve literatür taramasıydı. Bu aşamada, hem Microsoft’un hem de NVIDIA’nın yayınladığı teknik dökümantasyonları, örnek projeleri, makaleleri ve eğitim videolarını inceledik. Özellikle Microsoft’un DirectX-Graphics-Samples deposu ve NVIDIA’nın sunduğu DXR örnek projeleri, bize teknolojinin uygulama boyutunu anlamada çok yardımcı oldu.

İkinci aşama ise uygulamaların doğrudan incelenmesiydi. Bu noktada ilgili örnekleri indirip çalıştırdık, sahnelerin nasıl oluşturulduğunu ve ışınların nasıl işlendiğini adım adım gözlemledik. Her uygulamanın nasıl çalıştığını anlamaya çalışırken ekran görüntüleriyle belgeler oluşturduk.

Sonraki adımda, elde ettiğimiz verileri karşılaştırarak analiz ettik. Hem rasterization hem de ray tracing yöntemleriyle oluşturulan sahneleri karşılaştırmalı olarak inceledik. Farklı ışıklandırma ve yüzey materyallerinin ışın izleme üzerindeki etkilerini analiz ettik.

Son aşamadaysa bu çalışmaların çıktısını değerlendirerek raporlaştırdık. Projenin başında belirlediğimiz hedeflere ulaşıp ulaşmadığımızı kontrol ettik ve teknolojinin avantajlarını, zorluklarını ve gelecekte nasıl geliştirilebileceğini tartıştık.
## -------------------------------------------------------------

### 3. Grup Üyelerinin Görev Dağılımı
Bu projeyi bir ekip çalışması olarak yürüttük ve her bir grup üyesi, sürecin farklı aşamalarında aktif rol üstlendi. Ben öncelikle teorik araştırma ve literatür taramasından sorumluydum. Özellikle DirectX 12 Ray Tracing mimarisi ve API detayları üzerinde yoğunlaştım. Uygulamaların çalıştırılması ve demo görsellerin hazırlanması görevini de ben üstlendim. Bunun yanı sıra raporun yazımına ve sunumun hazırlanmasına aktif olarak katkıda bulundum.

Mehmet ise uygulamaların analiz edilmesi ve verilerin düzenlenmesinden sorumluydu. Çalışma sırasında ortaya çıkan çıktıları düzenli bir biçimde toplayıp raporladı. Ayrıca teorik araştırmalarda benimle birlikte çalışarak literatür taramasına katkı sağladı. Tüm bu süreç boyunca sunum materyallerinin oluşturulmasında da birlikte çalıştık.

### 4. DirectX 12 Nedir?
DirectX 12, Microsoft’un oyun geliştiricilere sunduğu en güncel grafik ve multimedya programlama arayüzüdür. Windows işletim sistemleri ve Xbox platformları için geliştirilen bu API, oyunlarda yüksek performanslı grafikler üretmek için kullanılır. Daha önceki sürümlerden farklı olarak, DirectX 12 geliştiricilere donanıma daha düşük seviyede erişim imkânı tanır. Bu da özellikle büyük ve karmaşık oyunlarda CPU ve GPU’nun daha verimli kullanılmasını sağlar.

Bir bakıma DirectX 12, geliştiriciler ile ekran kartı arasında bir köprü görevi görür. Geliştirici, yazdığı kodla doğrudan GPU’nun belirli kaynaklarına ulaşabilir ve grafik işlemlerini daha optimize bir şekilde gerçekleştirebilir. Bu özellik, çok çekirdekli işlemcilerde paralel işlemlerin daha etkin kullanılmasını sağlar ve bu sayede daha akıcı, daha hızlı oyun deneyimleri sunar.

### 5. Ray Tracing Nedir?
Ray tracing, yani ışın izleme, gerçek dünyadaki ışık davranışlarını simüle etmeye çalışan bir grafik tekniğidir. Bu yöntemde ışık, bir kaynaktan çıktıktan sonra sahnedeki nesnelere çarpar, yansır, kırılır veya gölgeler oluşturur. Yani, tıpkı gerçek hayatta olduğu gibi bir ışının camdan geçip yansıma yapması, metalden sekmesi ya da bir duvara gölge bırakması gibi detaylar hesaba katılır.

Ray tracing, geleneksel rasterization yöntemlerinden çok farklıdır çünkü sahnedeki tüm ışık hareketlerini gerçekçi biçimde izler. Bu da görüntülere adeta fotoğraf kalitesinde bir gerçekçilik kazandırır. Özellikle yansıma ve kırılma gibi karmaşık efektlerde ray tracing çok büyük avantajlar sunar.

Geleneksel rasterization ise bu tür detayları doğrudan çizimle elde eder. Bu yöntemde gölgeler ya da yansımalar ekstra hesaplamalarla simüle edilir, bu da çoğu zaman doğallığı bozar. Ray tracing ise fizik kurallarına dayalı hesaplamalarla bu efektleri otomatik olarak oluşturur.

6. DirectX 12 ile Ray Tracing (DXR)
DirectX Raytracing, yani DXR, Microsoft’un DirectX 12’ye entegre ettiği ray tracing uzantısıdır. Bu uzantı sayesinde geliştiriciler, ışığın sahne içinde nasıl davrandığını fiziksel olarak doğru biçimde simüle edebilirler. Bu da sahnelerin çok daha gerçekçi görünmesini sağlar.

DXR teknolojisinin üç temel bileşeni vardır: Acceleration Structures, Shader Binding Table ve çeşitli shader türleri. Acceleration Structures, sahnedeki nesnelerle ışınların çarpışma hesaplarını hızlıca yapabilmek için oluşturulan veri yapılarıdır. Shader Binding Table ise hangi ışının hangi shader tarafından işleneceğini belirleyen bir haritadır. Ray Generation, Miss ve Hit Shader’ları da ışınların sahnede nasıl yol aldığını, nereye çarpacağını ve nasıl bir sonuç döndüreceğini belirler.

NVIDIA’nın RTX ekran kartları, ray tracing işlemlerini hızlandırmak için özel olarak tasarlanmış RT Core adı verilen donanım birimlerine sahiptir. Bu çekirdekler sayesinde ışın-nesne çarpışmaları donanım düzeyinde hesaplanır ve bu da hem kaliteyi hem de performansı artırır.

Ayrıca, yüksek hesaplama gücü gerektiren bu işlem DLSS gibi yapay zekâ destekli teknolojilerle desteklendiğinde, hem yüksek FPS değerleri korunur hem de görsel kalite bozulmadan oynanabilirlik sağlanır.

7. Avantajlar ve Dezavantajlar
Ray tracing teknolojisinin en büyük avantajı, sunduğu görsel gerçekçiliktir. Işık efektleri, gölgeler ve yansımalar, fizik kurallarına göre işlendiği için sahneler sinematik bir kaliteye ulaşır. Özellikle metal yüzeylerdeki yansımalar, camlardaki kırılmalar ya da sudaki ışık oyunları, izleyiciye neredeyse gerçek bir dünya hissi verir.

Ancak bu kadar gerçekçilik, beraberinde ciddi bir işlem yükü de getirir. Ray tracing işlemleri, çok sayıda matematiksel hesaplama içerdiğinden güçlü bir ekran kartı gerektirir. Özellikle eski sistemlerde bu teknoloji kullanıldığında FPS değerleri ciddi şekilde düşebilir. Ayrıca kodlama tarafı da oldukça karmaşıktır; geleneksel yöntemlerle karşılaştırıldığında öğrenme eğrisi daha diktir.

Bu yüzden çoğu geliştirici, ray tracing’i tamamen değil, hibrit olarak yani rasterization ile birlikte kullanmayı tercih eder. Bu da hem performans hem de kalite açısından denge sağlar.

8-9. Demo Çıktıları ve Kodlar
Projede kullandığımız demo uygulamaları, doğrudan Microsoft’un ve NVIDIA’nın yayınladığı örnek projelerden alındı. Bu uygulamaları çalıştırarak, ışığın sahnede nasıl izlendiğini, nesnelerle nasıl etkileşime girdiğini ve elde edilen efektlerin ne kadar doğal göründüğünü gözlemledik. Demo kayıtları ve ekran görüntüleri, raporumuzda da yer aldı. Aynı zamanda demo kodları da incelenerek, bu efektlerin sahneye nasıl entegre edildiği üzerinde durduk.

10. Sonuç ve Değerlendirme
Sonuç olarak, bu proje bize DirectX 12 ve Ray Tracing teknolojisinin grafik dünyasında ne kadar önemli bir yer tuttuğunu çok net bir şekilde gösterdi. Hem teorik hem de uygulamalı olarak yaptığımız çalışmalar, bu teknolojinin grafik motorlarına nasıl entegre edileceğini ve donanımsal destekle nasıl daha verimli çalıştırılabileceğini ortaya koydu.

Elde ettiğimiz veriler, ray tracing’in görsel kalite açısından çok büyük avantajlar sunduğunu gösteriyor. Ancak yüksek donanım gereksinimi ve karmaşık yapısı, bu teknolojiyi her oyunda yaygınlaştırmayı henüz zorlaştırıyor. Yine de DLSS gibi destek teknolojiler sayesinde, yakın gelecekte bu tarz gerçekçi grafiklerin daha ulaşılabilir hale gelmesi oldukça olası.