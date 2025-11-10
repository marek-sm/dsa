"""
Problem: Remove Duplicates from Sorted List (LeetCode #83, Easy)
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-list/
Category: Linked List

Thoughts:
- I initially thought of using a dummy node to simplify the removal process, but it was not needed because the head node would never be a duplicate.
- I then knew to iterate through the linked list using a single while loop with the condition that the current node's next is not None.
- Inside the loop, I would compare the current node's value with the next node's value.
- If they are the same, I would skip the next node by adjusting the current node's next pointer to point to the next node's next.
- If they are different, I would simply move the current pointer to the next node.
- Later, I realized that I could adjust the loop condition to be that the current node and the current node's next are not None, which is a bit cleaner.
- The time complexity is O(N) because we may need to traverse the entire linked list once.
- The space complexity is O(1) as we are using a constant amount of extra space.

Approach:
- Initialize a current pointer to the head of the linked list.
- While the current pointer and the current pointer's next node are not None:
    - If the current node's value equals the next node's value, skip the next node by adjusting the current pointer's next to point to the next node's next.
    - Otherwise, move the current pointer to the next node.
- Return the head as the new head of the modified linked list.
"""

from typing import Optional

# -----------------------------
# Solution: Iterative In-Place Duplicate Removal - my solution
# Time Complexity: O(N)
# Space Complexity: O(1)
# -----------------------------
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next

        return head



if __name__ == "__main__":
    def to_list(h):
        out = []
        while h:
            out.append(h.val)
            h = h.next
        return out

    sol = Solution()

    # Test 1: Mixed duplicates
    head = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
    print(to_list(sol.deleteDuplicates(head)))  # [1, 2, 3]

    # Test 2: All unique
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    print(to_list(sol.deleteDuplicates(head)))  # [1, 2, 3, 4]

    # Test 3: All duplicates
    head = ListNode(7, ListNode(7, ListNode(7, ListNode(7))))
    print(to_list(sol.deleteDuplicates(head)))  # [7]

    # Test 4: Empty list
    print(to_list(sol.deleteDuplicates(None)))  # []