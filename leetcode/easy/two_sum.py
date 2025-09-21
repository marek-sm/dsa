"""
Problem: Two Sum (https://leetcode.com/problems/two-sum/)
Difficulty: Easy
Category: Array / Hash Table

Approach:
- Use a dictionary to store numbers and their indices.
- For each number, check if target - num exists in the map.

Time Complexity: O(n)
Space Complexity: O(n)
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