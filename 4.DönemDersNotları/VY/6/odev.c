#include <stdio.h>
#include <stdlib.h>

typedef struct Eleman {
    int katsayi;
    int us;
    struct Eleman* ileri;
} Eleman;

typedef struct Liste{
    int size;
    Eleman* bas;
    Eleman* son;
} Liste;

Eleman* yeniEleman(int katsayi, int us) {
    Eleman* yeni = malloc(sizeof(Eleman));
    yeni->katsayi = katsayi;
    yeni->us = us;
    yeni->ileri = NULL;
    return yeni;
}

Liste* yeniListe() {
    Liste* liste = malloc(sizeof(Liste));
    liste->bas = NULL;
    liste->son = NULL;
    liste->size = 0;
    return liste;
}

void listeyeEkle(Liste* liste, Eleman* eleman) {
    if (liste->bas == NULL) {
        liste->bas = eleman;
        liste->son = eleman;
    }
    else {
        eleman->ileri = liste->bas;
        liste->bas = eleman;
    }
    liste->size++;
}

Liste* polinomCarp(Liste* polinom1, Liste* polinom2) {
    Liste* sonuc = yeniListe();
    Eleman* i, * j;

    for (i = polinom1->bas; i != NULL; i = i->ileri) {
        for (j = polinom2->bas; j != NULL; j = j->ileri) {
            int yeniKatsayi = i->katsayi * j->katsayi;
            int yeniUs = i->us + j->us;

            Eleman* mevcut = sonuc->bas;
            Eleman* onceki = NULL;
            while (mevcut != NULL && mevcut->us != yeniUs) {
                onceki = mevcut;
                mevcut = mevcut->ileri;
            }

            if (mevcut == NULL) {
                Eleman* yeniElemanSonuc = yeniEleman(yeniKatsayi, yeniUs);
                listeyeEkle(sonuc, yeniElemanSonuc);
            }
            else {
                mevcut->katsayi += yeniKatsayi;
                if (mevcut->katsayi == 0) {
                    if (onceki == NULL) sonuc->bas = mevcut->ileri;
                    else onceki->ileri = mevcut->ileri;

                    if (mevcut == sonuc->son) sonuc->son = onceki;
                    sonuc->size--;
                }
            }
        }
    }

    return sonuc;
}

void polinomYaz(Liste* polinom) {
    Eleman* i;
    for (i = polinom->bas; i != NULL; i = i->ileri)
        printf("%dx^%d ", i->katsayi, i->us);
    printf("\n");
}

int main() {
    Liste* polinom1 = yeniListe();
    Liste* polinom2 = yeniListe();

    listeyeEkle(polinom1, yeniEleman(3, 2));
    listeyeEkle(polinom1, yeniEleman(4, 1));
    listeyeEkle(polinom1, yeniEleman(2, 0));

    listeyeEkle(polinom2, yeniEleman(1, 1));
    listeyeEkle(polinom2, yeniEleman(2, 0));

    printf("Polinom 1: ");
    polinomYaz(polinom1);
    printf("Polinom 2: ");
    polinomYaz(polinom2);

    Liste* carpimSonucu = polinomCarp(polinom1, polinom2);

    printf("Çarpım Sonucu: ");
    polinomYaz(carpimSonucu);

    return 0;
}
