#include "lists.h"
/**
 * insert_node -  inserts a number into a sorted singly linked list.
 * @head: pointer to the head of the list.
 * @number: the number that we want.
 * Return: adress of the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *min;
	listint_t *max;
	listint_t *new;
	
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	new->next = NULL;

	if (*head == NULL)
	{
		*head = new;
		return (new);
	}

	min = *head;
	max = (*head)->next;
	
	if ((*head)->n > number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	while (max)
	{
		if (min->n < number && number < max->n)
		{

			min->next = new;
			new->next = max;
			return (new);
		}
		min = max;
		max = max->next;


	}
	min->next = new;
	return (new);
}
