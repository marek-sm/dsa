"""
Problem: Sqrt(x) (LeetCode #69, Easy)
Link: https://leetcode.com/problems/sqrtx/
Category: Math / Binary Search

Thoughts:
- I initially thought to try each integer by iterating through them in a linear fashion until the square exceeds x.
- I then realized this would be relatively slow for large x, with a time complexity of O(sqrt(N)).
- I then realized binary search would be the optimal option, as integers are sorted by default.
- The time complexity is O(log(N)) because we halve the search space with each iteration.
- The space complexity is O(1) as we use a constant amount of variables.

Approach:
- Use binary search between 0 and x//2 + 1 (as the square root of x cannot be larger than x/2 for x > 1).
- Calculate the square of the mid-point and compare it to x.
- Adjust the search range based on the comparison.
"""

# -----------------------------
# Solution: Binary Search (Integer Square Root) - my solution
# Time Complexity: O(log(N))
# Space Complexity: O(1)
# -----------------------------
class Solution:
    def mySqrt(self, x: int) -> int:
        lo, hi = 0, x // 2 + 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            square = mid * mid
            if square == x:
                return mid
            elif square > x:
                hi = mid - 1
            else:
                lo = mid + 1
        return hi



if __name__ == "__main__":
    sol = Solution()
    print(sol.mySqrt(4))  # Output: 2
    print(sol.mySqrt(8))  # Output: 2
    print(sol.mySqrt(0))  # Output: 0
    print(sol.mySqrt(1))  # Output: 1
    print(sol.mySqrt(187))  # Output: 13