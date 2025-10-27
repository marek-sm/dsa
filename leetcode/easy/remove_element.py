"""
Problem: Remove Element (LeetCode #27, Easy)
Link: https://leetcode.com/problems/remove-element/
Category: Array / Two Pointers

Thoughts:
- Initially thought of using the pop method to remove elements equal to val, but this would be inefficient due to shifting elements.
- Realized, mainly because of my remove duplicates from sorted array solution, that I could use a two-pointer approach to overwrite elements not equal to val.
- This would allow me to do the operation in-place with O(1) extra space.
- After I wrote the solution, I researched if there was any more optimal solution, and there is one.
- It is sometimes faster because it minimizes the number of writes to the array by swapping elements equal to val with the last element in the current valid range.
- The time complexity is O(N) as we may need to check each element in the array.
- The space complexity is O(1) as we use a constant amount of extra space.

Approach:

Solution 1 (Two Pointer Overwrite): 
- Use two pointers to overwrite elements not equal to val.

Solution 2 (Swap-from-End):
- Use two pointers, one iterating through the list and the other tracking the end of the valid elements.
- When an element equal to val is found, swap it with the last valid element and reduce the size of the valid list.
- This method minimizes the number of writes to the array.
"""

from typing import List

# -----------------------------
# Solution 1: Two Pointer Overwrite - my solution
# Time Complexity: O(N)
# Space Complexity: O(1)
# -----------------------------
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k        

# -----------------------------
# Solution 2: Swap-from-End (Potentially Optimal) - not my solution
# Time Complexity: O(N), Space Complexity: O(1)
# -----------------------------
class SolutionTwo:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == val:
                nums[i] = nums[n - 1]
                n -= 1
            else:
                i += 1
        return n



if __name__ == "__main__":
    sol = Solution()
    print(sol.removeElement([3,2,2,3], 3))  # Output: 2
    print(sol.removeElement([0,1,2,2,3,0,4,2], 2))  # Output: 5

    sol2 = SolutionTwo()
    print(sol2.removeElement([3,2,2,3], 3))  # Output: 2
    print(sol2.removeElement([0,1,2,2,3,0,4,2], 2))  # Output: 5