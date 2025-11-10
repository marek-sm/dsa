"""
Problem: Merge Two Sorted Lists (LeetCode #21, Easy)
Link: https://leetcode.com/problems/merge-two-sorted-lists/
Category: Linked List / Recursion

Thoughts:
- I initially knew to create a dummy node to avoid needing to check for head separately.
- I then realized that I should use both linked lists not being None as the loop condition.
- Inside the loop, I would compare the values at the heads of both lists and attach the smaller one to the current node.
- After the main loop, I needed to attach the remainder of whichever list still had nodes left.
- After, I realized that I could optimize the solution by attaching the remainder in one step instead of looping through it.
- I could also use tuple unpacking to make the code cleaner when advancing the pointers.

Approach:

Solution 1 (Two tail-loops version):
- Use a dummy node to simplify edge cases.
- Iterate through both lists, attaching the smaller node to the merged list.
- After the main loop, use two separate loops to attach any remaining nodes from either list.
- Return the merged list starting from the node after the dummy.
- The time complexity is O(M+N), where M and N are the lengths of the two lists, as we may need to traverse both lists entirely.
- The space complexity is O(1) as we are only using a constant amount of extra space.

Solution 2 (Single-attach remainder version):
- Use a dummy node to simplify edge cases.
- Iterate through both lists, attaching the smaller node to the merged list.
- After the main loop, attach whichever list still has nodes in one step.
- Return the merged list starting from the node after the dummy.
- The time complexity is O(M+N), where M and N are the lengths of the two lists, as we may need to traverse both lists entirely.
- The space complexity is O(1) as we are only using a constant amount of extra space.
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# -----------------------------
# Solution 1: Two tail-loops version - my solution
# Time Complexity: O(M+N)
# Space Complexity: O(1)
# -----------------------------
class SolutionTwoLoops:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        while list1:
            current.next = list1
            list1 = list1.next
            current = current.next

        while list2:
            current.next = list2
            list2 = list2.next
            current = current.next

        return dummy.next

# -----------------------------
# Solution 2: Single-attach remainder version - not my solution
# Time Complexity: O(M+N)
# Space Complexity: O(1)
# -----------------------------
class SolutionSingleAttach:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                current.next, list1 = list1, list1.next
            else:
                current.next, list2 = list2, list2.next
            current = current.next

        # attach whichever list still has nodes
        current.next = list1 if list1 else list2
        return dummy.next



if __name__ == "__main__":
    def build_list(vals):
        dummy = ListNode()
        cur = dummy
        for v in vals:
            cur.next = ListNode(v)
            cur = cur.next
        return dummy.next

    def to_list(head):
        out = []
        while head:
            out.append(head.val)
            head = head.next
        return out

    # Test both solutions
    print("Testing SolutionTwoLoops:")
    sol1 = SolutionTwoLoops()

    l1 = build_list([1, 2, 4])
    l2 = build_list([1, 3, 4])
    print(to_list(sol1.mergeTwoLists(l1, l2)))  # [1, 1, 2, 3, 4, 4]

    l1 = build_list([])
    l2 = build_list([0])
    print(to_list(sol1.mergeTwoLists(l1, l2)))  # [0]

    l1 = build_list([])
    l2 = build_list([])
    print(to_list(sol1.mergeTwoLists(l1, l2)))  # []

    print("\nTesting SolutionSingleAttach:")
    sol2 = SolutionSingleAttach()

    l1 = build_list([1, 2, 4])
    l2 = build_list([1, 3, 4])
    print(to_list(sol2.mergeTwoLists(l1, l2)))  # [1, 1, 2, 3, 4, 4]

    l1 = build_list([])
    l2 = build_list([0])
    print(to_list(sol2.mergeTwoLists(l1, l2)))  # [0]

    l1 = build_list([])
    l2 = build_list([])
    print(to_list(sol2.mergeTwoLists(l1, l2)))  # []