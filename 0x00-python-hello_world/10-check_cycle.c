#include "lists.h"
/**
 * check_cycle - checks the linked list if it contains a cycle
 * @list: linked list thats checked
 *
 * Return: 1 list has a cycle, 0 no cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *slower = list;
	listint_t *faster = list;

	if (!list)
		return (0);

	while (slower && faster && faster->next)
	{
		slower = slower->next;
		faster = faster->next->next;
		if (slower == faster)
			return (1);
	}

	return (0);
}

