#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * check_cycle - checks for the cycle
 * @list: Pointer to list
 * Return: 0 if there is no cycle, 1 if not.
 */
int check_cycle(listint_t *list)
{
	listint_t *temp, *node;

	node = list;
	temp = list;
	while (node && temp && temp->next)
	{
		node = node->next;
		temp = temp->next->next;
		
		if (node == temp)
			return (1);
	}
	return (0);
}

