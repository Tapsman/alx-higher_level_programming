#include "lists.h"
/**
 * reverse_listint - A funtion that reverses a linked list
 * @head: The pointer to the first node
 * Return: Always a pointer to the first node that is in the
 * new list
 */
void reverse_listint(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *curr = *head;
	listint_t *next = NULL;

	while (curr)
	{
		next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
	}

	*head = prev;

/**
 * is_palindrome - A function that checks f the written linked list is
 * a linked list
 * @head: The pointer to the linked list
 * Return: 1 if it is a palindrome, 0 if it is not one
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, rapid = *head, temp = *head, *dup = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while(1)
	{
		rapid = rapid->next->next;
		if (!rapid)
		{
			dup = slow->next;
			break;
		}
		if (!rapid->next)
		{
			dup = slow->next->next;
			break;
		}
		slow = slow->next;
	}

	reverse_listint(&dup);

	while (dup && temp)
	{
		if (temp->n == dup->n)
		{
			dup = dup->next;
			temp = temp->next;
		}
		else
			return (0);
	}

	if (!dup)
		return (1);

	return (0);
}
