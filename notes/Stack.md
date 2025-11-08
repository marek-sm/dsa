# Stack

## TL;DR

A stack is a LIFO (last in, first out) data structure, meaning that the last node is the first one removed. This differs from a queue in that queues are FIFO (first in, first out), and a linked list in that you can't choose any node to add or remove. A stack is most useful for the undo/redo operations.

## When I’d choose it

- When the operations are focused on the last element.
- When the program has to do with the latest piece of data.
- When I need to backtrack through data.

## What I implemented

- push(item) — [Adds a node with data=item to the top of the stack]
- pop() - [Removes the node at the top of the stack]
- peek() - [Returns the data of the node at the top of the stack]
- is_empty() - [Returns true if the stack is empty, and false otherwise]

## Complexity

| operation | time | space | why (my words)                                       |
| --------- | ---- | ----- | ---------------------------------------------------- |
| push      | O(1) | O(1)  | There is no iteration and only one node is created.  |
| pop       | O(1) | O(1)  | There is no iteration and only one node is removed.  |
| peek      | O(1) | O(1)  | There is no iteration and only one node is returned. |
| is_empty  | O(1) | O(1)  | There is no iteration and only one node is checked.  |

## Mini trace

[] → push(15) → [15]
[15] → push(30) → [30, 15]
[30, 15] → peek() → 30
[30, 15] → pop() → [15]
[15] → is_empty() → False
[15] → pop() → []
[] → is_empty() → True

## Pitfalls I hit

- I initially forgot to implement the pop() method returning the popped value when it's called.
- I also forgot to account for the stack being empty in the peek() method, as before I added a check for self.head being None, it would have returned an error instead of None.
- Lastly, I mixed up self.head and self.head.data in the pop() method which would have caused a hash instead of the Node value being returned.

## Quick test plan I used

- When the stack is created it should have no nodes.
- The push method should successfully add a node to the beginning of the stack and the peek method should successfully return the head node value.
- The pop method should successfully remove the head node.
- The pop method should handle the case in which there are no nodes in the stack.
- The push method should function as expected even if the stack is empty.

## Sources I skimmed

- https://www.youtube.com/watch?v=wjI1WNcIntg
- https://www.youtube.com/watch?v=KcT3aVgrrpU
- ChatGPT
