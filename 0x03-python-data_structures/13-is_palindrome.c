#include "lists.h"

#define BUZSIZE 1024
/**
 * list_len - function that returns the number of elements in a linked list.
 * @h: pointer to head
 * Return: The number of elements (Nodes)
 */

int list_len(const listint_t *h)
{
	const listint_t *current = NULL;
	int counter = 0;

	current = h;
	while (current != NULL)
	{
		counter += 1;
		current = current->next;
	}
	return (counter);
}
/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: pointer to the header of a linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *aux = *head;
	int node1 = 0, node2 = 0, len = list_len(*head);
	int arrayOfNum[BUZSIZE];
	int status = 0;

	while (aux)
	{
		arrayOfNum[node1] = aux->n;
		aux = aux->next;
		node1++;
	}
	node1 = 0;
	node2 = len - 1;
	while (node1 < len)
	{
		if (arrayOfNum[node1++] == arrayOfNum[node2--])
			status = 1;
		else
			return (0);
	}
	if (status == 1)
		return (1);
	else
		return (0);
}
