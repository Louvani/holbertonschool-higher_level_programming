#include "lists.h"
/**
 * check_cycle - function that checks if a singly linked list has a cycle in it
 * @list: is the pointer to the list to check
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *faster = list;
	listint_t *slower = list;

	while (faster && slower && faster->next)
	{
		faster = faster->next->next;
		slower = slower->next;
		if (faster == slower)
		{
			return (1);
		}
	}
	return (0);
}
