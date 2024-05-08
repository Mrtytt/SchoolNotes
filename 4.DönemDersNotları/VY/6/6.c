#include <stdio.h>
#include <stdlib.h>

typedef struct node{
	int data;
	struct node* next;
}node;

typedef struct stack{
	int size;
	node* first;
}stack;

typedef struct stackArr{
	int bas;
	int size;
	int* stack;
}stackArr;

node* newNode(int value){
	node* new = malloc(sizeof(node));
	new->data = value;
	new->next = NULL;
	return new;
}

stackArr* newStackArr(int size)
{
	stackArr* new = malloc(sizeof(stackArr));
	new->size = size;
	new->stack = malloc(sizeof(int)*size);
	new->bas= -1;
	return new;
}

void pushArr(stackArr* stack,int value)
{
	if(stack->size != stack->bas)
	{
		stack->bas++;
		stack->stack[stack->bas] = value;
	}
}

stack* newStack(){
	stack* new =  malloc(sizeof(stack));
	new->first= NULL;
	new->size = 0;
	return new;
}

void push(stack* stack, node* new)
{
	stack->size++;
	new->next = stack->first;
	stack->first = new;
}

node* pop(stack* stack)
{
	node* temp = stack->first;
	if(temp)
	{
		stack->first = temp->next;
		stack->size--;
	}
	return temp;
}

node* popE(stack* stack)
{
	stack->first = stack->first->next;
}

void printStack(stack* stack)
{
	node* temp = stack->first;
	while(temp)
	{
		printf("%d ",temp->data);
		temp = temp->next;
	}
	printf("\n");
}

int main(void)
{
	stack* a = newStack();
	push(a,newNode(10));
	push(a,newNode(20));
	push(a,newNode(30));
	printStack(a);
}
