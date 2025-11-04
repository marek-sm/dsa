"""
Problem: Remove Linked List Elements (LeetCode #203, Easy)
Link: https://leetcode.com/problems/remove-linked-list-elements/
Category: Linked List / Recursion

Thoughts:
- I initially thought to first handle the edge case where the head nodes need to be removed.
- I figured it would be easier to use a dummy node to simplify the removal process, especially for head nodes.
- I then pondered using a double while loop: the outer loop to traverse the linked list and the inner loop to remove consecutive nodes with the target value.
- However, I realized that a single while loop would work just as well by checking the next node's value.
- The time complexity is O(N) because we may need to traverse the entire linked list once.
- The space complexity is O(1) as we are using a constant amount of extra space.

Approach:
- Create a dummy node that points to the head of the linked list.
- Initialize a current pointer to the dummy node.
- While the current pointer's next node is not None:
    - If the next node's value equals the target value, skip it by adjusting the current pointer's next to point to the next node's next.
    - Otherwise, move the current pointer to the next node.
- Return the dummy node's next as the new head of the modified linked list.
"""

from typing import Optional

# -----------------------------
# Solution: Iterative In-Place Removal (with Dummy Node) - my solution
# Time Complexity: O(N)
# Space Complexity: O(1)
# -----------------------------
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        current = dummy
        while current.next is not None:
            if current.next.val == val:
                current.next = current.next.next
                continue
            current = current.next
        
        return dummy.next



if __name__ == "__main__":
    def to_list(h):
        out = []
        while h:
            out.append(h.val)
            h = h.next
        return out

    sol = Solution()

    head = ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))
    print(to_list(sol.removeElements(head, 6)))  # [1, 2, 3, 4, 5]

    print(to_list(sol.removeElements(None, 1)))  # []

    head = ListNode(7, ListNode(7, ListNode(7, ListNode(7))))
    print(to_list(sol.removeElements(head, 7)))  # []