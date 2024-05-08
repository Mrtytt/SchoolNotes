## Listeler
- Alışveriş listeleri
- Aralarında doğrusal ilişki bulunur.
- Değişik türleri bulunur.
### Doğrusal Listeler (Diziler)
- Süreklilik, elemanlar aynı türde art arda saklanır.
- Arada başka eleman bulunmaz, ekleme işlemi sırasında yer değiştirme gerekir.
- Dinamik değildir, program başında tanımlanır.

- k'ninci elemanını silen algoritma
```c
void dizidenSil(int[] dizi, int k)
{
	int i;
	for(i = k; i<dizi.length - 1;i++)
	{
		dizi[i] = dizi[i+1];
	}
}
```

- k'ninci yerine yeni eleman ekleyen algoritma
```c
void diziyeEkle(int[] dizi,int k,int yeni)
{
	int i;
	for(i = dizi.lenght-2 ; i>=k ; i--)
	{
		dizi[i+1] =dizi[i];
	}
	dizi[k] = yeni;
}
```

- Sıralı bir dizide ikili arama yöntemiyle k sayısını arayan algoritma
```c
void dizideBul(int[] dizi,int k)
{
	int sol = 0;
	int sag = dizi.lenght-1;
	int orta = (sol+sag)/2

	while(sol<=sag)
	{
		if(k < dizi[orta]
			sag = orta - 1;
		else
			if(k > dizi[orta])
				sol = orta +1;
			else
				return orta
		orta = (sol + sag) / 2
	}
	return -1;
}
```

### Bağlı Listeler
![[Pasted image 20240421162430.png]]

- Bellekte ardışık olarak bulunmayan yapılar.
- Her eleman kendinden sonraki elemanın nerede olduğunu bilir.
- Bağlı liste dizisinin her elemanı bir struct nesnesidir.

```c
typedef struct node{
	int veri;
	struct* ileri;
}node;
```
- İki boyutlu dizi yapısı
- Silinen veri alanları hala listede yer alır, veri silindiği halde listenin boyu kısalmaz.
- Dinamik bir veri yapısına ihtiyaç vardır.
- 4 çeşittir.
	- Tek yönlü doğrusal bağlı liste 
	- İki yönlü doğrusal bağlı liste 
	- Tek yönlü dairesel bağlı liste 
	- İki yönlü dairesel bağlı liste
	
- Tam sayıları içeren bağlı liste
```c
typedef struct Eleman{
	int veri;
	struct* ileri;
	struct* geri;
}Eleman;
typedef struct list{
	int size;
	struct node* bas;
	struct node* son;
}list;

node* newEleman(int veri)
{
	node* new = malloc(sizeof(node));
	new->ileri = NULL;
	new->geri = NULL;
	new->veri = veri;
	return new;
}
list* newList()
{
	list* new = nalloc(sizeof(node));
	new->size = 0;
	new->bas = NULL;
	new->son = NULL;
	return new;
}
```

- Bağlı listenin başına eleman ekleme
```c
void listeninBasinaEkle(List* liste,Eleman* yeni)
{
	if(liste->son == NULL)
		son = yeni;
	yeni->ileri = bas;
	bas = yeni;
}
```

- Bağlı listenin sonuna eleman ekleme
```c
void listeninBasinaEkle(List* liste,Eleman* yeni)
{
	if(liste->bas == NULL)
		bas = yeni;
	else
		son->ileri = yeni;
	son = yeni;
}
```

- Liste başına, sonuna, ortasına eleman eklemek: O(1).

- Bağlı listenin ortasına eleman ekleme
```c
void listeninBasinaEkle(List* liste,Eleman* yeni,Eleman* once)
{
	yeni->ileri = once->ileri;
	once->ileri = yeni;
}
```

- Değer arama
```c
Eleman* listeAra(list* liste,int aranan)
{
	Eleman* temp = liste->bas;
	while(temp!= NULL)
	{
		if(temp->veri != aranan)
			temp = temp->ileri;
		else
			return temp;
	}
	return NULL;
}
```