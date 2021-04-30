#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: pointer to the pointer of the list
 * @number: Numbert to insert
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current_node = NULL;
	listint_t *new_node = NULL;

	if (!head)
		return (NULL);
	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);
	new_node->next = NULL;
	new_node->n = number;
	if (*head == NULL)
	{
		*head = new_node;
		return (new_node);
	}
	current_node = *head;
	if (number < current_node->n)
	{
		new_node->next = current_node;
		current_node = new_node;
	}
	while (current_node->next)
	{
		if (number > current_node->n && number <= current_node->next->n)
		{
			new_node->next = current_node->next;
			current_node->next = new_node;
		}
		current_node = current_node->next;
	}
	if (number > current_node->n && current_node->next == NULL)
	{
		current_node = new_node;
	}
	return (new_node);
}
