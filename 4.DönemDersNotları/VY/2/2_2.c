#include <stdio.h>
#include <stdlib.h>

struct deneme{
    int *X;
    int a;
    int b;
    struct deneme* denemep
};
typedef struct deneme Deneme;
typedef Deneme* Denemep;

int main(void){
    
    Deneme d1;
    Denemep dp;
    
    int y = 100;
    d1.a = 10;
    d1.b = 100;

    dp = (Deneme*)malloc(sizeof(Deneme));

    if(dp == NULL){
        printf("Memory can't be allocated\n");
        return 1;
    }
    free(dp);
}