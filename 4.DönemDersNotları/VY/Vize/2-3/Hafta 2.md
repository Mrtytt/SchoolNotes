## Algoritmik Program Tasarımı
- Adım adım uygulamayı tasarlama sürecidir.
- Akış şeması bunun grafiksel halidir.
### Özellikleri
- Etkin ve Genel Olma
- Sonlu Olma
- Kesinlik
- Doğruluk
- Giriş/Çıkış Tanımlı Olma
- Başarım (Verimli)
## Algoritma Süreci
- Tasarım
- Doğruluğunu ispat etme
- Analiz
- Uygulama
- Test
## Kaba-Kod (Pseudo Code)
- Yarı programlama dili, yarı konuşma dili.
- Algoritmayı genel olarak tasarlar.
## Algoritma Analizi
- Ne kadar süre veya ne kadar hızlı çalıştığına bakarız.
- Matematiksel bir ifade bulmak isteriz.
- İki önemli kavram var.
	- **Alan Karmaşıklığı** : Ne kadar yer kaplıyor.
	- **Zaman Karmaşıklığı** : Çalışma süresini
- Yapma sebebimiz en iyiyi bulmak.
### Yürütme Zamanı
- Bitene kadar geçen süredir
- n -> eleman sayısı ise yürütme zamanı **T(n)**
### Alan Maliyeti
- Kullanılan bellek miktarı.
- n elemanlı bir dizi elemanlarından her biri 4 byte ise alan maliyeti **T(n)=4n**
### Asimptotik Notasyonlar
- Zaman maliyetini ifade eder.
	- En İyi Durum (best case)
	- Ortalama Durum (average case) : Hesaplaması zordur.
	- En Kötü Durum : Hesaplaması kolaydır.
- Derecesi asimptotik notasyona verilir. **O(o),  Θ(o), Ω(o)** 
- **O(o)** : Üst sınır
- **Θ(o)** : Ortalama sınır
-  **Ω(o)** : Alt sınır
![[Pasted image 20240420215330.png]]

![[Pasted image 20240420215959.png]]

## Karmaşıklık
- Parametre karşısında algoritmanın değişimi gösteren ifadelerdir.
![[Pasted image 20240420220057.png]]

### Big-Oh (Asimptotik Üst Sınır)
#### Örnek 1
- x algoritması için Tx(N) = 1000N
- O notasyonu cinsinden çalışma süresi Tx(N)=1000N -> O(N)
- 1000N = O(N) ifadesini ispatlamak için;
- 1000N <=cN  
	- Her N>= n_{0}  eşitsizliğini belirli bir c ve n_{0} sabitleri için ispatlamak gerekir.
- c = 2000 ve n_{0} = 1 seçildiği zaman eşitsizliğin n_{0} dan büyük her N değeri için sağlandığı görülür.
#### Örnek 2 
- 7n2 + 5=O(n) ifadesinin doğruluğunu ispatlayınız. 
- O notasyonuna göre 7n2 + 5<=cn ∀n>=n0 olması gerekir. Bu şartı sağlayacak c ve n0 değerleri bulabilir miyiz? 
- Her iki tarafı n sayısına bölersek; 
- 7n+5/n <=c elde edilir. 
- Buna göre eşitliğin sağlanabilmesi için n sayısı değiştikçe c de değişmelidir. Sabit bir c ve n_{0} çifti yoktur. 
- Eşitsizlik doğru değildir.

### Notasyonu- Asimptotik Alt Limit (En iyi durum analizi) Ω(n)
- O notasyonunun tam tersidir.
### Θ(n) Notasyonu (Ortalama durum analizi)
### Püf Noktalar
- ![[Pasted image 20240420222155.png]] 
- ![[Pasted image 20240420222216.png]]
- ![[Pasted image 20240420222232.png]]
- ![[Pasted image 20240420232420.png]]
- ![[Pasted image 20240420232439.png]]
## Özyinelemeli Programların Analizi
- Analizi farklı
- Fonksiyonun çalışma süresine bağlıdır, programın çalışma süresi.
### Örnek 1
```c
int faktoriyel(int N)
	if(N <= 1)
		return 1;
	else 
		return N* faktoriye(N-1)
```
- N girdisi için çalışma süresi yine faktöriyel fonksiyonunun N - 1 girdisi için çalışma süresine bağlıdır.
- İkinci denklemdeki N yerine sırayla N − 1, N − 2, . . ., 2 koyarak
```c
	f(N) = f(N-1) + 1
	f(N-1) = f(N-2) + 1
	f(N-2) = f(N-3) + 1
		...
	f(2) = f(1) + 1
```
- Elde ederiz. Eşitlikleri taraf tarafa topladığımızda, f(N-1), f(N-2), . . . , f(2) sadeleşir ve geriye
```c
	f(N) = f(1) + N - 1
	f(N) = N elemandır O(N)
```

## Temel Teorem (Master)
- N büyüklüğünde bir problemi özyinelemeli çözmek için.
- N / b büyüklüğünde a tane alt problem çözüyor.
- Bu alt problemlerin çözümlerini de O(N^d) zamanda birleştirip ana probleme çözüm buluyorsak ana problemi çözmek için harcayacağımız zaman 
- ![[Pasted image 20240420235323.png]]
- ![[Pasted image 20240420235404.png]]
