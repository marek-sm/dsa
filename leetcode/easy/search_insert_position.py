"""
Problem: Search Insert Position (LeetCode #35, Easy)
Link: https://leetcode.com/problems/search-insert-position/
Category: Array / Binary Search

Thoughts:
- I initially knew this should be solved with a binary search, as the instructions specified a O(log(N)) time complexity.
- After implementing the binary search, I realized that if the target is not found, I need to indicate where it would be inserted.
- This could be done by returning the low pointer, as after the loop ends, it will have crossed the high pointer and will be at the correct insertion index.

Approach:
- Use a binary search to find the target in the sorted array.
- If found, return the index.
- If not found, return the low pointer as the insertion index.

Time Complexity: O(log(N)) because each step reduces the search space by half
Space Complexity: O(1) as I use a constant amount of variables
"""

from typing import List

# -----------------------------
# Solution: Lower Bound Binary Search - my solution
# Time Complexity: O(log(N)), Space Complexity: O(1)
# -----------------------------
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] > target:
                hi = mid - 1
            elif nums[mid] < target:
                lo = mid + 1
            else:
                return mid
        return lo

if __name__ == "__main__":
    sol = Solution()
    print(sol.searchInsert([1,3,5,6], 5))  # Output: 2
    print(sol.searchInsert([1,3,5,6], 2))  # Output: 1
    print(sol.searchInsert([1,3,5,6], 7))  # Output: 4