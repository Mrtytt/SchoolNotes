#include <stdio.h>
#include <stdlib.h>

typedef struct dugum{
	int veri;
	struct dugum*ileri;
}dugum;

typedef struct list{
	int size;
	dugum* bas;
	dugum* son;
}list;

dugum* yeni_dugum(int);

list* yeni_liste(void){
	list* liste = malloc(sizeof(dugum));
	liste->bas = NULL;
	liste->son = NULL;
	return liste;
}

void list_add_item_first(list* liste, dugum* dugumum)
{
	dugumum->ileri = liste->bas;
	liste->bas =dugumum;

	if(liste->son == NULL)
	{
		liste->son= dugumum;
	}
}

void list_add_item_between(list*liste,dugum*location,dugum*dugumum)
{
	dugumum->ileri = location->ileri;
	location->ileri = dugumum;

	liste->size++;	
}

int list_size(list* liste)
{
	int ctr = 0;
	dugum* start = liste->bas;
	while(start != NULL )
	{			
		ctr++;
		start = start->ileri;
	}
	if(liste->size!=ctr)
	{
		liste->size = ctr;
		printf("Not possible");	
	}
	return ctr;
}

void list_add_item_middle(list* liste, dugum* dugumum)
{
	int middle = list_size(liste);
	dugum* start = liste->bas;
	for(int i = 1;i<middle-1;i++)
	{
		start = start->ileri;
	}
	printf("BURADAYIM: %d\n",start->veri);
	list_add_item_between(liste,start,dugumum);
	
}

void list_add_item_last(list* liste,dugum* dugumum)
{
	if(liste->son==NULL)
	{
		liste->bas = dugumum;
	}
	else
	{
		liste->son->ileri = dugumum;
	}
	liste->son = dugumum;
	liste->size++;
}

void list_write(list* liste)
{
	dugum* start = liste->bas;
	while(start != NULL ){
		printf("%d->", start->veri);
		start = start->ileri;
	}
	printf("NULL\n");
}

int main(void){

	list* liste =yeni_liste();

	list_add_item_last(liste,yeni_dugum(10));
	list_add_item_last(liste,yeni_dugum(20));
	list_add_item_last(liste,yeni_dugum(30));
	list_add_item_first(liste,yeni_dugum(5));
	list_add_item_middle(liste,yeni_dugum(15));

	list_write(liste);
	return 0;
}
dugum* yeni_dugum(int value) {
    dugum* duguma = malloc(sizeof(dugum));
    duguma->veri = value;
    duguma->ileri = NULL;
    
    return duguma;
}
