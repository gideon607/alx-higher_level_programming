#include "lists.h"
/**
 * insert_node - Inserts number(S) into a sorted singly-linked list.
 * @head: A pointer to head of the linked list.
 * @number: number to be insert.
 *
 * Return: If function fails - then NULL.
 * Otherwise - a pointer to the new node or node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (node == NULL || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	new->next = node->next;
	node->next = new;

	return (new);
}
