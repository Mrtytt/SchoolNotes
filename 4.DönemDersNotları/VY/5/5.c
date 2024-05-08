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
void list_remove_first_item(list* liste) {
	if (liste->bas == NULL) {
		// Liste zaten boş
		return;
	}
	dugum* gecici = liste->bas;
	liste->bas = liste->bas->ileri;
	free(gecici);
	liste->size--;

	if (liste->bas == NULL) {
		// Liste boşsa, son düğümü de güncelle
		liste->son = NULL;
	}
}
void list_remove_last_item(list* liste) {
	if (liste->bas != NULL) {
		if (liste->bas->ileri == NULL){
			// Tek eleman varsa
			free(liste->bas);
			liste->bas = NULL;
			liste->son = NULL;
		}
		else{
			dugum* gecici = liste->bas;
			while (gecici->ileri->ileri != NULL) {
				gecici = gecici->ileri;
			}
			free(gecici->ileri);
			gecici->ileri = NULL;
			liste->son = gecici;
		}
		liste->size--;
	}
}

int list_size(list* liste){
	int ctr = 0;
	dugum* start = liste->bas;
	while(start != NULL ){			
		ctr++;
		start = start->ileri;
	}
	if(liste->size!=ctr){
		liste->size = ctr;
		printf("Not possible");	
	}
	return ctr;
}
void list_remove_middle_item(list* liste){
	int middle = list_size(liste);
	dugum* start = liste->bas;
	dugum* once = liste->bas;
	once = NULL;
	for(int i = 1;i<middle-1;i++)
	{
		once = start;
		start = start->ileri;
	}
	once->ileri=start->ileri;
	free(start);
}
int list_remove_item(list* liste,int aranan){
	dugum* once = liste->bas;
	dugum* temp = liste->bas;
	once=NULL;
	while(temp){
		if(temp->veri==aranan){
			once->ileri=temp->ileri;
			return aranan;
		}
		once=temp;
		temp=temp->ileri;
	}
	printf("Değer bulunamadı.");
}
void list_add_item_middle(list* liste, dugum* dugumum){
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
