#include <stdlib.h>
#include <stdio.h>

typedef struct Node {
	int data;
	struct Node* left;
	struct Node* right;
}Node;

typedef struct Tree{
	Node* root;
}Tree;

Node* newNode(int data){
	Node* node = malloc(sizeof(Node));
	node->data = data;
	node->left = NULL;
	node->right = NULL;
	return node;
}
Tree* newTree(){
	Tree* tree = malloc(sizeof(Tree));
	tree->root = NULL;
	return tree;
}
Node* search(Node* node, int aranan){

	Node* temp = node;
	while(temp){
		if(temp->data < aranan)
		{
			temp = temp->right;
		}
		else if(temp->data < aranan)
		{
			temp = temp->left;
		}	
		else{
			return temp;
		}
	}
	return temp;
}
Node* searchR(Node* node, int aranan){

	if(!node)
		return NULL;
	if(node->data == aranan)
		return node;
	if(node->data>aranan)
		return searchR(node->left,aranan);
	return searchR(node->right,aranan);
}

Node* min(Tree* tree){
	Node* temp= tree->root;
	while(temp->left){
		temp=temp->left;
	}
	return temp;
}
Node* minR(Node* node){
	if(!node)
		return NULL;
	if(!node->left)
		return node;
	return minR(node->left);
}
Node* max(Tree* tree){
	Node* temp= tree->root;
	while(temp->right){
		temp=temp->right;
	}
	return temp;
}
Node* maxR(Node* node){
	if(!node)
		return NULL;
	if(!node->right)
		return node;
	return minR(node->right);
}
void ekle(Tree* tree, Node* node){
	Node* temp = tree->root;
	Node* n = NULL;
	while(temp)
	{
		n=temp;
		if(temp->data>node->data){
			temp= temp->left;
		}
		else
			temp=temp->right;
		if(n == NULL)
			n = node;
		if(node->data>n->data)
			n->right = node;
		else
			n->left = node;
	}
}
//Silerken soldakinin en büyüğünü veya sağdakini en küçüğü
void sil(Tree* tree,int data)
{
	Node* temp, n=tree->root;
	while(n->data!=data){
		if(n->data>data)
			n=n->left;
		else
			n=n->right;
	}
	while(1){
		temp=maxR(n->left)
		if(temp==NULL)
			temp=minR()
	}
}	
