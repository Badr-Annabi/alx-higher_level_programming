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
	listint_t *temp;


	temp = list;
	while (temp != NULL)
	{
		temp = temp->next;
		if (temp->next == list)
			return (1);
		else
			temp = temp->next;
	}
	return (0);
}

