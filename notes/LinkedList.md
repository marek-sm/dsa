# Linked List (Singly)

## TL;DR

A linked list is a data structure made up of nodes, which store data and point to each other, with the first node being called the head. A linked list differs from an array in that while arrays are indexed, linked lists are only connected by its nodes pointing to each other.

## When I’d choose it

- Prepending a node, as it is O(1), while it would be O(N) in an array as every element would have to move one to the right.
- Inserting a node when the reference is known, as that would also be O(1).
- Deleting a node when the reference is known, as that would too be O(1).

## What I implemented

- prepend(value) — [Prepends a node to the linked list, making it the "head" node]
- append(value) — [Appends a node to the linked list, functioning by iterating through the linked list until it reaches the last node]
- delete(value) — [Deletes the first node which data equals the value supplied in the method call]
  The three methods account for when the list is empty by either creating a first Node for it or by returning when there is nothing to delete, and there is a special case in the delete method to delete the head.

## Complexity

| operation | time | space | why (my words)                                                      |
| --------- | ---- | ----- | ------------------------------------------------------------------- |
| prepend   | O(1) | O(1)  | There is no iteration and only one node is created.                 |
| append    | O(N) | O(1)  | The list needs to be iterated through but only one node is created. |
| delete    | O(N) | O(1)  | The list needs to be iterated through but only one node is created. |

## Mini trace

[] → prepend(10) → [10]
[10] → prepend(30) → [30, 10]
[30, 10] → append(50) → [30, 10, 50]
[30, 10, 50] → delete(10) → [30, 50]

## Pitfalls I hit

- At first, I forgot to account for the edge case in which the head of the node needs to be deleted, causing the code to not run. I simply solved this by assigning the first node to the second one.
- I also had neglected to update the variable "current" in the append method, leading to an infinite loop in many cases. This was easily fixed by incrementing current by 1 with each iteration.
- I initially compared current.next == value instead of current.next.data == value, causing the delete method to fail as instead of comparing its data, it compared a Node object. I fixed this by always comparing against the node's .data field.

## Quick test plan I used

- When the linked list is created it should have no nodes.
- The prepend method should work with both an empty linked list and one with nods already in it, adding a node to the front, making it the head node.
- No node should point to the node which is deleted.
- The head node, any middle node, and the tail node should be able to be deleted by the delete method.
- Attempting to delete a node that doesn't exist should do nothing.
- The Prepend and append methods should work as intended.

## Sources I skimmed

- https://www.youtube.com/watch?v=F8AbOfQwl1c&pp=ygUVd2hhdCBpcyBhIGxpbmtlZCBsaXN0
- https://www.youtube.com/watch?v=njTh_OwMljA&pp=ygUVd2hhdCBpcyBhIGxpbmtlZCBsaXN0
- ChatGPT
