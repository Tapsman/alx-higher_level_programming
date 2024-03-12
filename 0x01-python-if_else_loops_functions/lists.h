#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>
/**
 * struct listint_s - A singly linked list
 * @n: Is the integer
 * @next: Pointer to the nxt node
 * Description: Singly linked list node
 */
typedef struct listint_s
{
        int n;
        struct listint_s *next;
} listint_t;
size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int n);
void free_listint(listint_t *head);
listint_t *insert_node(listint_t **head, int number);
#endifi
