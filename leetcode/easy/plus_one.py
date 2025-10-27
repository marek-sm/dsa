"""
Problem: Plus One (LeetCode #66, Easy)
Link: https://leetcode.com/problems/plus-one/
Category: Array / Math

Thoughts:
- I initially knew that I would need to either add one to the last digit or handle the carry if the last digit is 9.
- I decided to use a reverse loop, through the digits from the end to the beginning, adding one to the last digit and handling the carry if necessary.
- This results in a time complexity of O(N) in the worst case (when all digits are 9) because it needs to evaluate each element, and a space complexity of O(1) since the input list is modified in-place.
- The time complexity is O(N) because in the worst case, we may need to iterate through all digits.
- The space complexity is O(1) because we are modifying the input list in place.

Approach:
- Loop through the digits from the end to the beginning.
- If the current digit is 9, set it to 0 and continue to the next digit.
- If the current digit is not 9, add one to it and return the modified list.
- If the loop completes and all digits were 9, we need to add a new digit at the beginning of the list (1 followed by zeros).
"""

from typing import List

# -----------------------------
# Solution: Carry-based loop - my solution
# Time Complexity: O(N)
# Space Complexity: O(1)
# -----------------------------
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        return [1] + digits



if __name__ == "__main__":
    sol = Solution()
    print(sol.plusOne([1, 2, 3]))  # Output: [1, 2, 4]
    print(sol.plusOne([4, 3, 2, 1]))  # Output: [4, 3, 2, 2]
    print(sol.plusOne([9]))  # Output: [1, 0]  