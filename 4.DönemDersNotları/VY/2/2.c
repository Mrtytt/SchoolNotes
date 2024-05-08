#include <stdio.h>

struct deneme{
    int a;
    float b;

    struct ahmet{
        int c;
    }
    struct deneme* d
}c; --> direk c olarak tanımlanabilir.

int main(void){

    deneme x;
    x->a=100;
    
    struct deneme* d;
    d=&x;

    typedef struct deneme D --> her defa yazmammak için yaptık;
    typedef D* dp;

    return 0;
}