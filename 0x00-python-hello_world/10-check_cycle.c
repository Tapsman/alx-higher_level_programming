#include "lists.h"
/**
 * check_cycle - A function to check if linked list
 * contains a cycle
 * @list: The linked list to check in
 * Return: 1 if list has cycle, 0 on not
 */
int check_cycle(listint_t *t)
{
	listint_t *steady = list;
	listint_t *rapid = list;

	if (!list)
		return (0);
	while (steady && rapid && rappid->next)
	{
		steady = steady->next;
		rapid = rapid->next->next;
		if (steady == fast)
			return (1);
	}
	return (0);
}
