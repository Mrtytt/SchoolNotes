## İki Listeyi Birleştirme 
```c
Liste* birleştir(list* l1, list* l2)
{
	List* temp = malloc(sizeof(node));
	if(l1->bas == NULL)
		return l2;
	if(l2->bas == NULL)
		return l1;
	temp->bas = l1->bas;
	temp->son = l2->son;
	l1->son->ileri = l2->bas;
	return temp;
}
```

## Çift Bağlı Liste
- İki yönlü bağ vardır.
- İki taraflı adres tutar.
```c
typedef struct node
{
	int veri;
	struct Node* ileri;
	struct Node* geri;
}node;
node* newNode(int veri)
{
	node* new = malloc(sizeof(node));
	new->veri = veri;
	new->ileri = NULL;
	new->geri = NULL;
	return new;
}
typedef struct list
{
	int size;
	struct Node* bas;
	struct Node* son;
}list;
list* newList()
{
	list* new = malloc(sizeof(node));
	new->size = 0;
	new->bas = NULL;
	new->son = NULL;
	return new;
}
```

- Başına eleman ekleme
```c
	void basaEkle(Liste* liste, Node* node)
	{
		if(liste->son == NULL)
			liste->son = node;
		else
			liste->bas->geri = node;
		node->ileri = liste->bas;
		liste->bas = node;
	}
```

- Sonuna eleman ekleme;
```c
	void sonaEkle(Liste* liste, Node* node)
	{
		if(liste->bas == NULL)
			liste->bas = node;
		else
			liste->son->ileri = node;
		node->geri = liste->son;
		liste->son  = node;
	}
```

- Ortaya eleman ekleme;
```c
	void ortayaEkle(Liste* liste,Node* yeni, Node* once)
	{
		yeni->ileri = once->ileri;
		yeni->geri = once;
		once->ileri->geri = yeni;
		once->ileri = yeni;
		
		liste->size++;
	}
	
```

## Dairesel Bağlı Liste
```c
	typedef struct dlist
	{
		int size;
		struct Node* bas;
	}dlist;
	dlist* newdList()
	{
		dlist* new = malloc(sizeof(node))
		new->bas = NULL;
		new->size = 0;
		return new;
	}
```

```c
	void add(liste* dairelist, node* yeni)
	{
		if(liste->bas == NULL)
		{
			yeni->ileri = yeni;
			yeni->geri = yeni;	
		}
		else
		{
			yeni->ileri = liste->bas;
			yeni->geri	
		}
	}
```