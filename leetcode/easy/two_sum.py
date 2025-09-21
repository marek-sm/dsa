"""
Problem: Two Sum (LeetCode #1, Easy)
Link: https://leetcode.com/problems/two-sum/
Category: Array / Hash Table

Thoughts:
- Used a brute force method in the past, which is O(n^2).
- In this solution I utilized a hash map / dictionary to store previously seen numbers.
- This allows for O(1) average time complexity lookups allowing a O(n) time complexity.
- While a dictionary uses more space, it is worth the trade-off for the time complexity improvement.

Approach:
- Use a dictionary to store numbers and their indices.
- For each number, check if target - num exists in the map.

Time Complexity: O(n) as the list is scanned once
Space Complexity: O(n) because a dictionary is used to store complements
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pastNums = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in pastNums:
                return [pastNums[complement], index]
            else:
                pastNums[num] = index  

if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([2, 7, 11, 15], 9))  # Output: [0, 1] 