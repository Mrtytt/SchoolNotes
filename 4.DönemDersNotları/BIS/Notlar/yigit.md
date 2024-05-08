### Sanallaştırma:

- Mevcut sistemde farklı sistemler kurarak yeni işletim sisteminin kurulması diyebiliriz. Yani VM diyebiliriz.

- VM'lere emulatör denir ve bu sınavda karşına çıkabilir aklında tut.

- Bunun başka örneklerine de bakarsın.

### Complier ve interpreter arasındaki fark:

- Complier dili makine diline çevirir (dil compile edilebiliyorsa)

- interpreter yorumlayıcıdır bu mesela java'dır önce anlaşılabilir dile çevirir sonrasında bu şekilde işlem daha hızlı ilerler.(Compileye göre)

- Basic gibi bazı diller hem compile hem de interpreter edilebilir yani bazı komutlar yorumlanır bazıları da compile edilir.


### Software as a Service (SaS):

- Yazılımın servis sunmasıdır.

- Google Collab buna güzel bir örnektir.


### Embeded sistemler:

- Akıllı evler falan filan gibi şeylerin etraftaki sensörlerden alınan verileri yorumlayıp bazı işlemlerin yapılmasını sağlar.

- En çok gerçek zamanlı sistemlerde kullanılır.

- CPU yerine FPGA kullanılır.

- Maliyetleri yüzünden rasberry pi gibi sistemler kullanılmaya başlandı.

- Zaman hassasiyeti yüksektir.



### İşletim sistemi sistemleri:

- Dosya sistemi sayesinde sistemler disk üzerinde belli ölçüde işlemler yapabilir.

- Accounting sistem yani yeni hesaplar açılabilir.

- Program execution programların başlatılmasını sağlar.

- I/O operasyonları.

- Communication sistemler bağımsız processler arasında iletişimi sağlar.

- Protection and Security; protection iç sistemde korumayı sağlar, security dışarıdan korur.

- Resource allocation.

- Error detection.

- System calların sistemlere iletilmesini OS yapar.


#### Bach: 

- Birden çok dosyayı işleyebilme.

#### İlk GUI 1973 Xerox Alto bilgisayarda kullanılmıştır sınav test olursa bu soru olarak çıkar.

### Sistem çağrıları:

- Bir dosyayı açmak, kapamak ve içeriğini okumak bir sistem çağrısıdır.

- Dosya kaydedilince dosya servisi çağrılır.

- USB'ye kaydedince ilk dosya servisi sonrasında I/O servisi çağrılır.

- Windows'ta CreateProcess() fonksiyonu, kernelde NTCreateProcess() sistem çağrısını çalıştırır.

- Sistem çağrıları için veri girişi gerekebilir ve 3 yöntem kullanılabilir:
	1. Registerler
	2. Hafızada blok veya tablo
	3. Stack

- Sistem çağrıları 6 tane grubu ayrılır:
	1. Process control:
		- end(), abourt(), load(), execute() bazı komutlarıdır. Komutlar test sınavında garnati gelir.
		- Bir process sonlandırılırsa bir hata mesajı verilir ve loga kaydedilir.
		- Debugger program logları kontrol eder ve bug düzeltilir.
		- Birden fazla program aynı veriyi kullanabilir bu durumda kullanmakta olan process veriyi kilitler ve diğer processler erişemez.
		- Kilitleme için acquire lock() salarken ise release lock() sistem çağrıları ile yapılır.
		- Process control multi ve single tasking sistemlerde farklı gerçekleşir.
		- Çok görevli işleitm sistemlerinde command interpter sürekli çalışır bu şekilde multi tasking yapar.
	2. File managment
	3. Device manager:
		- Erişim isteği request(), işin tamamlanması halinde release() komutu kullanılır.
		- Erişim sağlandığında read() ve write() ile okuma ve yazma işlemleri gerçekleştirilir.
	4. Information maintenence:
		- Örneğin date(), time() gibi sistem çağrıları kullanıcı programına gerekli bilgileri atar.
		- Diğer sistem çağrıları, anlık kullanıcı sayısı, işletim sistemi versiyonu gibi verileri verir.
	5. Communication:
		- İletişim için 2 yöntem kullanılır:
			1. Message-passing model- Mesajlar processler arasında doğrudan veya dolaylı (mesaj kutusu) gönderebilir: (Bu yöntem 2'ye oranla daha güvenlidir)
				- Her process için bir ID ve process adı vardır.
				- open connection() ve close connection() çağrıları kullanılır. (Burası önemli)
				- Her process gelen mesajları kabul etmek için accepet connection() çağrısı kullanılır. (Burası önemli)
				- Client ve server olarak adlandırlır.
			2. Shared memory:
				- Hafıza alanı oluşturmak için shared memory create() ve erişmek için shared memory attach() sistem çağrıları kullanılır.
	6. Protection:
		- Bilgisayar sistem kaynaklarına erişimi kontrol eden mekanizmaları sağlar.
		- Çok kullanıcılı ve multiprogramming sistemleri için kullanılır.
		- Günümüzde bütün cihazlarda vardır.
		- Erişim yetkilendirmesi için set permission() ve get permission() sistem çağrıları kullanılır.
		- İzin vermek veya izni kaldırmak için allow user() ve deny user() sistem çağrıları kullanılır.
- Test olursa üsttekilerin komutları garanti çıkar yani EZBERLE. Slaytta ayrıntıları var.

### Sistem programları (system utilities)
- En altta **donanım**,
- Sonra **işletim sistemi**,
- Sonra **sistem programları**,
- En son **uygulama programları** vardır.
- Program geliştirme ve çalıştırma için alan oluşturur:
	- **File managment:**
		- Dosya ve dizinlerde, create, delete, copy, rename, print, list, ... gibi işlemler gerçekletirir.
	- **Status information:**
		- Bazı programlar tarih, kalan alan, saat, hafıza gibi bilgileri ister.
		- Daha karmaşık programlar performans, log gibi verileri ister.
	- **File modification:**
		- Disk veya diğer saklama birimlerindeki verileri değiştirme, görüntüleme amacıyla kullanılan metin editörleri vardır.
	- **Programming language support:**
		- Programlama dillerini supportlar.
	- **Program loading/execution:**
		- Bir program derlendikten sonra hafızaya yükleyip çalıştırmak için kullanılır.
		- Makine dilinde veya yüksek seviyeli diller için debug amacıyla kullanılabilir.
	- **Communications:**
		- Processler, kullanıcılar ve bilgisayarlar arasındaki konuşmalardan sorumludur.
	- **Background services:**
		- Tüm genel amaçlı sistemler boot sırasında bazı sistem programlarını çalıştırır (Tamamı değil bazıları çalışır yani tetiklenmeyi bekler **BU MADDE ÖNEMLİ**).
		- Sistem başladıktan sonra **bazı processler sonlandırılır bazıları ise sistem kapanana kadar devam eder**.
		- Bu tür sistem programları **service, subsystem veya daemon** olarak adlandırlır.
			- Test olursa bu madde çıkabilir.
		- Ağ bağlantısı, yazıcı işlemleri, sistem hata izleme servisleri sistem programlarını sağlar.

### İşletim sistemi tasarımı ve gerçekleştirilmesi
- **Mekanizmalar ve kurallar:**
	- Kurallar (policies) ne yapılacağını, mekanizmalar (mechanisms) nasıl yapılacağına karar verir (**Sınavda çıkar**).
	- Örneğin; CPU'nun korunması için timer kullanımı **mekanizma**, bir kullanıcının timer süresine ne kadar olacağına karar vermesi ise **kuraldır**.
	- Kurallar, kaynak ayırmasında oldukça önemlidir.
- Implementation:
	- Belirlenen gereksinimler, kurallar ve mekanizmaları göz önünde bulundurarak kodlama aşamasıdır.
	- İşletim sistemleri daha hızlı olması için assembly kullanılır.
	- İlk işletim sistemleri yine assembly kullanılmıştır.
	- MS-DOS 8088 assembly diliyle yazılmış ve sadece intel x86 işlemcilerince çalışır.
	- Linux C ile yazılmıştır ve intel x86i Oracle SPARC ve IBM PowerPC işlemcileriyle çalışabilir.
	- Üstteki 2 maddede anlıyoruz ki yüksek seviyeli diller başka işlemcilerle rahatlıkla çalıştırılabilir ama daha yavaş ve daha fazla alan kullanır.

### Kernel:
- İşletim sisteminin ana bileşenidir.

#### İşletim sistemi yapısı (mimarisi):
- Sistemin düzgün çalışması tasarımına bağlıdır.
- Tasarım olarak birden fazla kernel tasarımı vardır.

##### Monolitik (basit) yapı:
- En eski ve yaygın mimaridir.
- Bu sistemin temel özelliği işletim sisteminin tüm servislerini -bir bileşen olarak- çekirdek içinde aynı seviyede tutar.
- MS-DOS ve Unix bu tiptendir.
- Her şey tek levelde tutulduğundan bir sistem hata verdiğinde bütün sistem hata verebilir.
- Günümüzde çok kullanılmaz.
- MS-DOS uygulama programları I/O rutinerline rahatlıkla erişebiliyor ve bu özellik yüzünden kötücül bir program girdiğinde tüm sistemi patlatıyor.

##### Katmanlı yapı:
- İşletim sistemlerinin zaman geçtikçe daha fazla servise ihtiyacı olmuştur bunun üzerine bu yapı oluşturulmuş.
- En alt katmanda donanımla ilgili servisler varken en üstte kullanıcı arayüzü vardır.
- Bir katmanda bir güncelleme sonrası tüm kernelin compile edilmesi gerekir.
- Katman sayısı değişebilir ama olabildiğince az tutulup sistem hafif tutulmaya çalışılır.
- Her katman bir alttaki katmanın fonksiyonunu kullanabilir bu olumlu olsa da sistem hep başka katmanlara fonksiyonu soracağından sistemi yavaşlatır.

##### Micro kernel:
- UNIX geliştirildikçe kernel çok fazla büyümüştür.
- Bunun üzerine Mellon Üniversitesinde mikro kernel yaklaşımıyla **Mach** adında işletim sistemi geliştirilmiştir.
- Bu yüzden kernel içindeki acil olmayan her şey sistem programlarına (kullanıcı düzeyine) aktarılmıştır.
- Bu yapıda çoğu servis kullanıcı olarak çalıştığından gerektiğinde o kullanıcı kapatılarak o sistemin güvenliğini daha iyi sağlar.

##### Modüler:
- Günümüzde en çok kullanılandır.
- Kernel boot sırasında veya sistemin çalışması devam ederken yüklenen bileşenlere sahiptir.
- Bir modül kendisi yüklendikten sonra başka modülleri çağırabilir veya iletişime geçebilir.
- Linux cihaz sürücüleri ve dosya sistemleri için yüklenebilir kernel modülleri kullanır.

##### Hibrit:
- Her kernel yapısından birer parça alarak yapmıştır.
- Günümüzde tek yapı halinde olmadığından her bir yapıdan birer parça alınmıştır.
- Örneğin Linux ve Solaris monolitich yapıdadır ama kernel kısmına yeni fonksiyonlar dinamik olarak eklenebilir.
- Günümüzde çoğu işletim sistemi bunu kullanır.
- Bu tip yapılarda çekirdek zayıflatılır ve gelişmiş görevler için dinamik modüllerin eklenmesine izin verirler. ÖNEMLİ

###### Mac OS X:
- İlk sürümü 1984
- Hibrit sisteme sahiptir.
- En üst katmanda Aqua kullanıcı arayüzü vardır.
- İkinci katmanda uygulama geliştirme platformları ve servisleri vardır.
- Cocoa: Objective C diline API sağlar.
- Kernel BSD kernel ile Mach kerneline sahiptir.

###### IOS:
- Mac OS X üzerine kurulmuş Applenin mobil sistemleri için gleiştirilmiştir.
- Core OS; en alt katmandır.

###### Android:
- Linux kernel kullanır.
- En alt katmanda process yönetimi, cihaz sürücüleri ve power managment için kullanılır. 

##### Exokernel (Dış çekirdek):
- Uygulama geliştiriciler için işletim sisteminin temel fonksiyonlarından birisi olan donanıma erişim yordamlarını ve donanım sürücülerini devre dışı bırakıp direkt donanıma girer.
- Özel amaçlar dışında çok kullanılmaz.

### İşletim sistemi debugging:
- Hata ayıklama sistemidir.
- Performance tuning olarak da isimlendirilebilir.
- Hata analizi:
	- Hata loga kaydedilir.
	- İşletim sistemi aynı zamanda hafızanın anlık durumunu da (memory dump) kaydeder.
	- Memory dump belleğin hangi kısmında neler olduğunu kaydeder kısacası.
	- **Kernelde** ortaya çıkan hata **crash** olarak adlandırılır.
	- Debugging, bir kodu yazmaktan çok daha zordur.
- Performance tuning:
	- Sistem performansını arttırmak için yapılır.
	- Sistem tıkanıklıklarını giderir.

### İşletim sistemi üretilmesi:
- Çok bir şey yok slaytlardan bakarsın

### Sistem boot:
- Kernelden yüklenerek bilgisayarın başlatılmasına booting denir.
- Bootstrap programı, ROM üzerinde ve işletim sisteminin kernel kısmını yükler (Sınavda çıkabilir.).
- Büyük işletim sistemlerinde bootstrap ROM'da, işletim sistemi ise diske kaydedilir.
- Boot kısmına sahip olan diske boot sik veya system disk olarak adlandırılır.

### Process kavramı:
- Modern işletim sistemlerinde process bir işin parçacığını belirtir.
- CPU, aralarında geçiş yaparak tüm processlerin eş zamanlı olarak çalıştırabilir.
- Bir sistem tek kullanıcılı olsa bile birden fazla uygulamayı(excel, word, ...) birlikte çalıştırabilir.
- İşletim sistem multitasking desteklemese bile işletim sisteminin **kendi fonksiyonlarını çağırarak** multitasking yapabilir. Mesela **context switch** yaparak multitasking yapabilir.
- Context Switch sınavda çıkar yine aklında dursun.
- Bir programı çalıştırdığımızda önce bir process oluşturulur sonra o uygulama ile process ilişkilendirilir yani gerekli kod parçacıkları processe aktarılır.
- Kısacası process programlardan bağımsız kavramlardır program çalıştırılmak istendiğinde program parçacıkları processe aktarılır ve böylece program çalışır.
- İşletim sistemi daha hızlı çalışmak için önceden hazırda tuttuğu processleri boşta tutar.
- Bir process sadece ama sadece bir programla ilişkilendirilir ancak çalışma sırasında bu ilişkilendirme değiştirilebilir yani atıyorum chromu a processinde başlattın sonra a processi başka bir şey için gerekti o zaman chromu b processine aktarabilirsin.
- Bir process, yürütmekte olduğu işi, program counteri, CPU register değerlerini içermektedir.
- Bir process tamamen halt edilene kadar tekrar tekrar kullanılabilir ki alttaki işlemler tekrar tekrar kullanılmasına gerek olmasın.

#### Process oluşturma adımları:
-  Metin editörü
- Ön işlem adımı (derlemeye hazırlık diyebilir)
- Linkerlar yani başka dosyalarla bağı varsa bağlanır.
- Yükleme (belleğe yüklenir)
- CPU

#### Process aşağıdaki bileşenleri içerir:
- Stack, fonksiyon parametreleri, return adresleri, ve lokal değişkenler.
- Data section, global değerleri saklar.
- Heap, processe runtime'da dinamik olarak atanan bellektir.

#### Process çalıştığı sürece durumları değişir:
- New: Process oluşturulur.
- Running: Komutlar çalıştırılmaktadır.
- Waiting: Process bir olayın gerçekleşmesini beklemektedir. (I/O bir cihazdan bildirim)
- Ready: Process çalışmak için CPU'ya gönderilmesini bekliyor.
- Terminated: Process çalışamsı sonlandırılır.
- **Kuyruk veri yapısı** kullanılır.

#### Process control block:
- Bir process, işletim sisteminde process control block tarafından temsil edilir.
- Oluşturduğu şeyler:
	- Process state
	- Process number / Process ID her process'in kendine has ID'si vardır.
	- Process counter
	- Register
	- Memory limits
	- List of open files
	- ...

### Process planlama
- Çok programlı sistemlerde tamal amaç CPU'nun maks sürede çalışmasıdır.
- Zaman paylaşımlı sistemlerde CPU çok kısa aralıklarla processler arasında geçiş yapar.
- Bir processin CPU'da çalışıp çalışmayacağını process scheduler seçer.

#### Scheduling queues:
- Bir process sisteme girdiğinde tüm işlerin bulunduğu job queue'ye girer.
- Hafızaya alınmış çalışmayı bekleyen processler ready queue'ye alınır.
- Kuryruk yapıları genelde linked list şeklinde tutulur.
- Devamı slaytta ve bu sınavda çıkarmış.
- Child processin oluşturulmasının yapılmasının sebebi mevcut processi hafifletmektir.
- Process I/O isteğinde bulunursa I/O kuyruğuna alınmış olur.
- Bir process başka bir process çalıştırırsa onun bitmesini bekler.
- Bir process çalışması için ayrılan süre ... Devamı slaytta

#### Scheduler:
- Bir process çalışması süresi boyunca kuyruklar arası gezinebilir.
- Processlerin seçilmesi scheduler tarafında belirlenir.
- Batch sistemlerde çok sayıda process çalıştırılmak üzere sisteme gönderilir.
- Bu processler disk üzerinde biriktirilir ve daha sonra çalıştırılır.
- Long-term scheduler bu işleri seçerek çalışmak üzere hafızaya yükler.
- Short-term CPU'ya alınacak hazırda bekleyen processleri seçer.
- Short-term scheduler çok kısa aralıklarla ve sıklıkla çalışır, Long-term  ise dakika aralığında çalışır.
- Üstteki 3 madde çıkabilir.
- Processler I/O bound ve CPU-bound olarak 2'ye ayrılır.
- I/O boundlar I/O işlemleri için daha fazla süre ayırır. I/O queue dolar ready queue boşalır
- CPU-bound CPU ile hesaplama işlemleri için daha fazla süre ayırır. Ready queue dolar.
- Windows ve Unix sistemler Long-term çok kullanmaz daha çok short term kullanır.

#### Context switch:
- Context switch sırasında belli bir miktar zaman CPU çalışmaz bu süreye overhead denir, sınavda çıkabilir.

#### Process creatin:
- Processler dinamik olarak oluşturulur ve silinirler.
- Bir parent process child process oluşturduğunda yeni child process CPU time, hafıza, dosyalar ve I/O cihazları gibi kaynaklara ihtiyaç duyar.
### Paralelizm hakkındaki slayta bak bir önceki derste hoca onu işlemiş
### İşlemler arası iletişim için kullanılan ilk mekanizmalar
- İşlemler arası sinyal gönderilebilmesi için gerekli yetkiye sahip olması lazım. Yani her process'in sinyal gönderme yetkisi yoktur.
- Unix'te root'un full sinyal gönderme yetkisi vardır.
- Mesela bir hata gerçekleştiğinde işlemciye hata sinyali gönderilir.
- Bir işlemin başka bir işleme sinyal gönderebilmesi için her iki işlemin de aynı process grubu içinde veya aynı kullanıcı içinde olması lazım. #Önemli
- Bir sinyalin bir işlem tarafından alıgalanabilmesi ve işleenbilmesi için sinyalin blokelenmemiş olması (try-catch) ve çalışması kesilebilir (interruptable) surumda olması lazım.
- Bir sinyalin oluşması için çalıştırılan fonksiyona signal handler denilir.
#### Boru hattı (pipe line):
- İşlemler arası bir yönlendirme denilebilir.
- Bir işlem için çıktı öbür işlem için girdi olarak kullanıyorsa olur ve tek yönlüdür.
- Aynı parente ait işlemlerde olur.
- Ebevyen pipe() sistem çağrısıyla pipe line'yi başlatır sonra fork() ile kendi kopyasını oluşturur (child oluşturur).
- Tek yönlü bir iletişim vardır yani Parent child'a sinyal gönderebilirken child parente gönderemez.
### İşlemler arası iletişim nesnelerinin kalıcılığı
1. İşlem seviyesinde kalıcılık:
	- Process çalıştığı sürece obje hayatını devam ettirir.
	- İhtiyaç kalmazsa önceden de sonlandırılabilir. #Önemli
	- Boru türü nesneler örnek olarak verilir.
2. İşletim seviye kalıcılık:
	- İşletim sistemi çalıştığı sürece devam eder. 
	- Yani process sonlansa bile yine çalışmaya devam eder yani çalışmaya hazır halde bekler. #Önemli 
	- Mesaj kuyrukları, semaforlar ve paylaşımlı bellekler örnek verilebilir.
3. Dosya seviyesinde kalıcılık:
	- Varlıklarını devamlı olarak sürdürürler. 
	- İşletim sistemi kapatılsa bile varlıklarını sürdürürler
	- Dosya silinirse bir tek varlıklarını devam ettiremez. #Önemli 
	- POSIX mesaj kutuları, paylaşılan belgeler, ...
#Not POSIX ile mesaj kuyruğu, paylaşılan bellek, semaforlar, pipeler barındırılır
### Multi-threading modelleri
- Çalışabilmesi için kernel moda geçilip kernel thread ile user thread arasında ilişkilendirme modellerinden birini kullanmalı #Önemli :
	- Çoktan bire:
		- Eğer bir thread sistem çağrısı bloklarsa tüm process blokklanır.
		- Aynı anda sadece bir tane kullanıcı thread'i kernel thread'ine erişir
	- Birden çoğa:
		- Biri bloklanırsa öbürleri çalışmaya devam eder.
		- Multicore sistemlerde eşzamanlı çalışmasına izin verilir.
		- Kötü yanı çok sayıda kernel thread oluşur ve karmaşıklık artar.
	- Çoktan çoğa:
		- User thread kernel thread'den daha fazla olur genelde.
		- Birden çoğa'nın sorunları çözülür.
		- Bir thread bir sistem çağrısını bloklarsa kernel başka bir threadi çalıştırır.
	- İki seviyeli model:
		- Hem çoktan çoğa hem de birden bire modeli eşleştirir.
		- Solaris OS 9. sürüm #örnek
#### Thread kütüphaneleri
- Programcıya thread oluşturmak ve yönetmek için API sağlar.
- Kütüphaneyi oluştururken 2 yaklaşım vardır:
	1. Tüm kütüphane kullanıcı alanda oluşturulur ve kernel desteği yoktur.
	2. İşletim sisteminin doğrudan desteklediği kernel seviyesinde kütüphane oluşturulur.
- İki strateji vardır:
	1. Asenkron threading:
		- Threadler arasında veri paylaşımı az olduğunda kullanılır.
		- Yeni child oluşturulduğunda çalışmalarını eşzamanlı olarak devam ettirebilirler
	1. Senkron threading:
		- Parent child başladığında processini durdurur bunlar tamamlandığında çalışmasına devam eder.
		- Threadler arasında veri paylaşımı fazla olduğunda kullanılır
- Günümüzde 3 temel kütüphane vardır #Önemli:
	1. POSIX 
	2. Windows 
	3. Java:
		- #Önemli parameter passerle ilgili madde önemli.
#Not Bunların tam olarak nasıl çalıştığı slaytlarda var ve orası da önemlidir.
#### Dolaylı thread oluşturma
- Çok sayıda thread ile uygulama yapmak zordur.
- Thread oluşturma işi geliştirici yerine compiler tarafından yapılması günümüzde giderek popüler hale gelmektedir.
- Bu stratejiye implict (üstü kapalı) threading olarak tanımlanır.
- Thread pool:
	- Multithread bir web sunucusu, gelen isteklerin her birisi için yeni thread oluşturur.
	- Çok sayıda istek aynı anda gelirse sistem kaynakları çok çabuk dolar.
	- Bunun önüne geçmek için sistem önceden hazırda tuttuğu threadler vardır bu şekilde yeni thread oluşturmak için kaybedilecek zamanın önüne geçilir.
	- Sistem belli sayıda thread hazırda tutmasıdır kısacası.
- OpenMP:
	- C, C++ ve fortran için yazılmış bir grup compiler direktiftir.
	- Shared memory ykalaşımı kullanır.
	- OpenMP ile \#pragma omp paralel direktifi kullanılır #Önemli 
- Grand Central dispatch:
	- Apple sistemleri için OpenMP diyebiliriz.
	- Dispatch queue serial veya concurrent (Eşzamanlı çalışma) şeklinde oluşturulabilir #Önemli 
	- FIFO çalışır ve sadece bir blok kuyruktan alınır.
	- Concurrnet queue FIFO çalışır ve kuyruktan birden fazla blok aynı anda alınabilir.
	- 3 farklı kuyruk yapısı vardır: #Önemli 
		- Low (Önemli değil)
		- Default (Orta düzey önemde)
		- High (Mümkün olduğunca hızlı corede koşulması lazım)
#### Thread çalıştıma kuralları
- Signal handling:
	- Threadler yaptıkları işlemler için iletişim kurmak ister.
	- Unix sistemlerde sinyaller belirli bir olayın gerçekleştiğini belirtir.
	- Oluşan olaya karşılık sinyal bir processe iletilir.
	- Sinyal senkron veya asenkron alınabilir.
	- Senkron sinyal, sinyalin oluşmasına neden olan olayı gerçekleştiren processe iletilir.
		- İllegal hafıza erişimi veya 0'a bölme #örnek 
	- Asenkron sinyal, sinyali oluşturan processten başka bir processe iletilir.
	- Sinyaller process içindeki farklı hedeflere gönderebilir:
		- Bir threade
		- Tüm threadlere
		- Bazı threadlere
- Thread iptal etme: #örnek 
	- İşlem tamamlanmadan iptal edilebilir. 
	- İstenen bir sonucun bir threadin tarafından bulunması sonucu iptal edilebilir. 
	- Bir web sayfasaına girerken stop tuşuna basılırsaprocess içindeki tüm threadler iptal edilir. 
	- Bir thread çalışırken başka bir thread aniden onu sonlandırabilir. #Önemli 
	- Bir thread başka bir threadin kendi kendisini doğal biçimde iptal etmesini sağlayabilir.
#not Vizede 7 slayttan sorumluyuz.
#### Windows ve linux threadleri
##### Windows threadleri:
- Temel api olarak Windows API kullanır.
- thread için şu thread komutları kullanır:
	- ETHREAD: Thread çalıştırılır
	- KTHREAD: Kernel ile ilgili kısımlar
	- TEB: User kısımdadır ve uygulama çevresi olarak tanımlanabilir
##### Linux threadleri:
- clone() veya fork() ile sistem çağrısı ile thread oluşturabilir #Önemli 
- fork() ile yeni görev başlattığında parent task veri yapısı kopyalanır. clone() ile ise istediğin gibi kısıtlamalar yapılabilir.
#### Process senkronizasyonu
- Cooperative processler diğer processleri etkileyebilir veya diğer processlerden etkilenebilir.
- Bunlar paylaşılmış hafıza veya dosya sistemleri ile veri paylaşımı yaparlar.
- Paylaşımlı veriye eşzamanlı erişim tutarsızlık problemlerine yol açabilir. Aynı anda değişiklik yapılırsa bu gerçekleşir yani iletişim yoksa bu olur. #Önemli 
- Bu yöntem yavaştır çünkü ilk virtual memorye bakar sonrasında kalan hafızaya bakmak zorundadır.
- Gelişigüzel veriye erişilmeli yani planlama yapılmalı.
- Paylaşılan veriye erişim üretici - tüketici ilişkisi olarak gösterilebilir. Öncelikle üretilmeliki tüketilsin.
- Bir işleme ait iş parçacıklarına micro işlem denir.
#### Eşzamanlılık (Concurrency): #Önemli 
- Eş zamanlı process olması durumunda bu 4 madde önem kazanır:
	- Processler arası haberleşme
	- Kaynak paylaşımı
	- Birden fazla processin senkronizasyonu
	- İşlemci zaman atanması
- Sorunlar:
	- Bir processin çalışma hızı öngörülemez:
		- Diğer processlerin yaptıklarına bağlıdır.
		- İşletim sisteminin kesmeleri nasıl ele aldığına bağlıdır mesela bazılarına görmezden gel ya da beklet falan diyebilir.
		- İş sıralama yaklaşımına bağlıdır.
- Çözüm:
	- Kaçırdım
- Processlerin etkileşimi:
	- Birbirinden habersizlerse: Rekabet
	- Birbiriden dolaylı olarak haberleri vardır: Paylaşma yoluyla işbirliği
	- Processlerin direkt birbirinden haberi vardır: Haberleşme yoluyla işbirliği
