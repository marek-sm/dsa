"""
Problem: Palindrome Number (LeetCode #9, Easy)
Link: https://leetcode.com/problems/palindrome-number/
Category: Math / String

Thoughts:
- Recognized almost instantly that I could simply convert the string to an integer and compare it to its reverse.
- Python makes it easy to do so with slicing.
- I then saw that LeetCode challenged me to do it without converting to a string.
- I attempted to do so but could not get the right solution, so I researched the optimal solution.
- The optimal solution happens to be the half-reverse method, which has a space complexity of O(1) instead of O(n)
- Although the optimal solution has the same time complexity of O(n), it is more efficient as it only processes half of the digits.
- With a space complexity of O(1) as it has a constant amount of variables, it is much more efficient in terms of memory usage as well.

Approach:

Solution 1 (Slicing): 
- Compare the integer converted to a string to its reverse using slicing.

Solution 2 (Half Reverse):
- Return False if the number is negative or ends in a zero and is not zero, as a number greater than zero cannot begin with zero.
- Reverse half of the number using a sequence of modulus and integer division operations.
- Compare the reversed half to the remaining half. If the number has an odd number of digits, remove the middle digit by integer dividing the reversed half by 10.
"""

from typing import List

# -----------------------------
# Solution 1: Slicing - my solution
# Time Complexity: O(n), Space Complexity: O(n)
# -----------------------------
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1] 

# -----------------------------
# Solution 2: Half-Reverse (Optimal) - not my solution
# Time Complexity: O(n), Space Complexity: O(1)
# -----------------------------
class SolutionPalindromeOptimal:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
        return x == reversed_half or x == reversed_half // 10

if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome(121))  # True
    print(sol.isPalindrome(-121)) # False
    print(sol.isPalindrome(10))   # False
    print(sol.isPalindrome(-101)) # False

    sol_optimal = SolutionPalindromeOptimal()
    print(sol_optimal.isPalindrome(121))  # True
    print(sol_optimal.isPalindrome(-121)) # False
    print(sol_optimal.isPalindrome(10))   # False
    print(sol_optimal.isPalindrome(-101)) # False