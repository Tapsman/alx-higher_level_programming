#include "lists.h"
/**
 * check_cycle - A function to check if linked list
 * contains a cycle
 * @list: The linked list to check in
 * Return: 1 if list has cycle, 0 on not
 */
int check_cycle(listint_t *list)
{
	listint_t *steady = list;
	listint_t *rapid = list;

	if (!list)
		return (0);
	while (steady && rapid && rapid->next)
	{
		steady = steady->next;
		rapid = rapid->next->next;
		if (steady == rapid)
			return (1);
	}
	return (0);
}
