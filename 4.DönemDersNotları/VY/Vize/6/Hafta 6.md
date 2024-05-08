- Bağlı listeler ile stack tanımı 
```c
	typedef struct node
	{
		int veri;
		struct node* ileri;
	}node;
	
	node* newNode(int veri)
	{
		node* new = (node*)malloc(sizeof(node));
		new->veri = veri;
		new->ileri = NULL;
		return new;
	}
	
	typedef struct stack
	{
		struct node* ust;
	}stack;
	
	stack* newStack()
	{
		stack* new = (stack*)(malloc(sizeof(stack)));
		new->ust = NULL;
		return new;
	}
	
	stack peek(stack* stack)
	{
		return stack->ust->veri;
	}
	
	bool stackbos(stack* stack)
	{
		if(stack->ust == NULL)
			return true;
		else
			return false;
	}
	void push(stack* stack,node* node)
	{
		node->ileri = stack->ust;
		ust = node;
	}
	void pop(stack* stack)
	{
		if(!stackbos())
		{
			stack->ust = stack->ust->ileri
		}
	}
```