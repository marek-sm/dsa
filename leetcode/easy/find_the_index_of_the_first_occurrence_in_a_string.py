"""
Problem: Find the Index of the First Occurrence in a String (LeetCode #28, Easy)
Link: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
Category: Two Pointers / String / String Matching

Thoughts:
- Initially thought of simply using Python's built-in .find() method, which is very efficient and concise.
- However, I wanted to implement a more manual approach to understand the underlying mechanics.
- I realized that I could use the length of the "needle" string to create substrings of the "haystack" and compare them.
- There were many opportunities to make off-by-one errors, but I carefully adjusted the range of the loop to ensure it only checked valid starting positions.
- This brute-force method involves checking each possible starting position in the "haystack" where the "needle" could fit.
- Although this method is less efficient than using built-in functions, it provides a clear understanding of string matching.

Approach:

Solution 1 (Brute Forcing / Naive Search): 
- Check if the length of the needle is greater than the haystack; if so, return -1.
- Iterate through the haystack up to the point where the needle could still fit.

Solution 2 (Built-in .find()):
- Use Python's built-in string method .find() to locate the needle in the haystack.
"""

# -----------------------------
# Solution 1: Brute Forcing / Naive Search - my solution
# Time Complexity: O(M*N), Space Complexity: O(1)
# -----------------------------
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        
        for i in range(len(haystack) - (len(needle) - 1)):
            if haystack[i:len(needle) + i] == needle:
                return i
        
        return -1

# -----------------------------
# Solution 2: Built-in .find() - Simple Python Method
# Time Complexity: O(M+N), Space Complexity: O(1)
# -----------------------------
class SolutionTwo:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)



if __name__ == "__main__":
    sol = Solution()
    print(sol.strStr("sadbutsad", "sad"))  # Output: 0
    print(sol.strStr("leetcode", "leeto"))  # Output: -1

    sol2 = SolutionTwo()
    print(sol2.strStr("sadbutsad", "sad"))  # Output: 0
    print(sol2.strStr("leetcode", "leeto"))  # Output: -1