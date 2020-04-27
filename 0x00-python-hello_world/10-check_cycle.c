#include "lists.h"
/**
 * check_cycle - checks for a cycle in a linked list
 * @list : linked list to check
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *traverse;

	if (list && list->next)
		traverse = list->next;
	else
		return (0);

	while (list && traverse)
	{
		if (list == traverse)
			return (1);

		list = list->next;

		if (traverse->next)
			traverse = traverse->next;

		else
			return (0);
		if (traverse->next)
			traverse = traverse->next;
		else
			return(0);
	}
	return (0);
}
