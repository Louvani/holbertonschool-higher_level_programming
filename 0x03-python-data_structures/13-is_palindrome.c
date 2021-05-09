#include "lists.h"
#include <stdio.h>

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: pointer to the header of a linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *aux = *head;
	int node1 = 0, node2 = 0, len;
	int arrayOfNum[BUFSIZ];
	int status = 0;

	while (aux)
	{
		arrayOfNum[node1] = aux->n;
		aux = aux->next;
		node1++;
	}
	if (node1 == 0 || node1 == 1)
		return (1);
	node1 -= 1;
	len = node1;
	while (node2 < len)
	{
		if (arrayOfNum[node2++] == arrayOfNum[node1--])
			status = 1;
		else
			return (0);
	}
	return (status);
}
