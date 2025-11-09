# Queue

## TL;DR

A queue is a FIFO (first in, first out) data structure, meaning that the first node is the first one removed. This differs from a stack in that stacks are LIFO (last in, first out), and a linked list in that you can't choose any node to add or remove. A queue is most useful for task scheduling.

## When I’d choose it

- When the operations being "first come first serve" is ideal.
- When the data resembles a waiting line.
- When it relates to streaming/buffering.

## What I implemented

- enqueue(item) — [Adds a node with data=item to the end of the queue]
- dequeue() - [Removes the node at the start of the queue]
- peek_front() - [Returns the data of the node at the start of the queue]
- is_empty() - [Returns true if the queue is empty, and false otherwise]

## Complexity

| operation  | time | space | why (my words)                                       |
| ---------- | ---- | ----- | ---------------------------------------------------- |
| enqueue    | O(1) | O(1)  | There is no iteration and only one node is created.  |
| dequeue    | O(1) | O(1)  | There is no iteration and only one node is removed.  |
| peek_front | O(1) | O(1)  | There is no iteration and only one node is returned. |
| is_empty   | O(1) | O(1)  | There is no iteration and only one node is checked.  |

## Mini trace

[] → enqueue(15) → [15]
[15] → enqueue(30) → [15, 30]
[15, 30] → peek_front() → 15
[15, 30] → dequeue() → 15
[30] → is_empty() → False
[30] → dequeue() → 30
[] → is_empty() → True

## Pitfalls I hit

- I initially forgot to implement the dequeue() method returning the popped value when it's called.
- I also forgot to account for the case in which the list becomes empty again, as self.tail was not being reset, leading to the enqueue() method not recognizing the list as empty.
- Lastly, I mixed up self.head and self.head.data in the dequeue() method which would have caused a hash instead of the Node value being returned.

## Quick test plan I used

- When the queue is created it should have no nodes, the is_empty() method should return True, and the peek_front() method as well as the head and tail nodes should return None.
- The enqueue method should successfully add a node to the end of the queue and the peek_front method should successfully return the head node value.
- The dequeue method should successfully remove the head node.
- The dequeue method should handle the case in which there are no nodes in the queue.
- The enqueue method should function as expected even if the queue is empty.
- The is_empty() method should return False when there are nodes in the queue.

## Sources I skimmed

- https://www.youtube.com/watch?v=wjI1WNcIntg
- https://www.youtube.com/watch?v=D6gu-_tmEpQ&t=1s
- ChatGPT
