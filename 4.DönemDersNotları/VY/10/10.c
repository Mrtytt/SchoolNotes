#include <stdio.h>
#include <stdlib.h>

typedef struct node{
    int value;
    struct node;
}node;

typedef struct tree{
    node* root;
    
}tree;

int main(void){
    return 1;
}