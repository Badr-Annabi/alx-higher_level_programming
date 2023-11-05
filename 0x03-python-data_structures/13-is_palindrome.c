#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: pointer to the first node of the list.
 * Return: 1 if the list is a palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *fast = *head;
	listint_t *slow = *head;
	listint_t *first_half = NULL;
	listint_t *tmp = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;

		tmp = slow->next;
		slow->next = first_half;
		first_half = slow;
		slow = tmp;
	}
	if (fast != NULL)
		slow = slow->next;

	while (first_half != NULL && first_half->n == slow->n)
	{
		slow = slow->next;
		first_half = first_half->next;
	}
	if (first_half == NULL)
		return (1);
	else
		return (0);
}
