"""
Problem: Remove Duplicates from Sorted Array (LeetCode #26, Easy)
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
Category: Array / Two Pointers

Thoughts:
- Initially thought of using a set to remove duplicates, but that would not maintain the order, use extra space, and was ultimately would not be needed as the array is already sorted.
- I then thought of manually removing duplicates, but that would take extra time and space and is unnecessary.
- Finally, I realized I could use two pointers to update the array in place when a unique number is found.
- The first pointer (i) would iterate through the array, while the second pointer (k) would track the position to place the next unique number.

Approach:
- Initialize a pointer k to 1, which will track the position of the next unique element.
- Iterate through the array starting from the second element (index 1) using a pointer i.
- For each element, compare it with the previous element.
- If the current element is different from the previous one, it is unique.
- Assign the current element to the position indicated by k and increment k.
- After the loop, k will represent the number of unique elements in the array.
- Return k as the result.

Time Complexity: O(N) because I iterate through N elements in the array
Space Complexity: O(1) as I use a constant amount of variables
"""

from typing import List

# -----------------------------
# Solution: Two Pointers - my solution
# Time Complexity: O(N), Space Complexity: O(1)
# -----------------------------
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k += 1
        return k

if __name__ == "__main__":
    sol = Solution()
    print(sol.removeDuplicates([1,1,2]))  # Output: 2
    print(sol.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))  # Output: 5