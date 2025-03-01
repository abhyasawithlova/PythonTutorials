# Linked Lists

## Types
- Singly Linked List
- Doubly Linked List
- Circular Linked List

## Linked List Operations.
### Append and PrePend nodes
### Delete Node
### Search for Key

## Here are some key edge cases to keep in mind while reversing a Linked List.

**Empty List:** If the linked list is empty (i.e., the head is None), your reverse function should handle this gracefully without attempting to access any nodes.

**Single Node:** If the linked list contains only one node, reversing it should result in the same list, and your function should handle this without issues.

**Two Nodes:** If the linked list contains exactly two nodes, reversing it should properly swap the head and tail pointers and update the next and prev references.

**Odd and Even Number of Nodes:** Ensure that your reverse function works correctly for both odd and even numbers of nodes in the list.

**Cyclic List:** If your linked list is cyclic (i.e., the tail node points back to one of the previous nodes), your reverse function should handle this case and avoid infinite loops. Typically, you would first need to break the cycle before reversing the list.

**Maintaining Integrity:** After reversing the linked list, verify that all next and prev references are correctly updated and that the list can be traversed from both the new head to the new tail and vice versa without any issues.