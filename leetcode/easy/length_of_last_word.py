"""
Problem: Length of Last Word (LeetCode #58, Easy)
Link: https://leetcode.com/problems/length-of-last-word/
Category: String

Thoughts:
- Initially knew I could use the Python split method to break the string into words and return the length of the last word.
- This would have a time complexity of O(N) and space complexity of O(N), because it needs to iterate through the entire string and store each word in a list.
- After implementing this, I researched if there was a more optimal solution.
- I found a two-pointer approach that only requires O(1) space, as it does not need to store the words and only needs to iterate through as much of the string as necessary.
- As necessary is defined as the length of the last word plus any trailing spaces; this is still O(N) time complexity in the worst case, but it is more efficient in terms of space, because it only uses a constant amount of extra space.

Approach:

Solution 1 (Split-based) - my solution: 
- Use the split method to break the string into words and return the length of the last word.

Solution 2 (Two Pointers) - not my solution
- Use two pointers to skip trailing spaces and then count the length of the last word.
"""

# -----------------------------
# Solution 1: Split-based - my solution
# Time Complexity: O(N)
# Space Complexity: O(N)
# -----------------------------
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        return len(words[-1])        

# -----------------------------
# Solution 2: Two Pointers - not my solution
# Time Complexity: O(N)
# Space Complexity: O(1)
# -----------------------------
class SolutionTwo:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1

        # 1) skip trailing spaces
        while i >= 0 and s[i] == ' ':
            i -= 1

        # 2) count the last word length
        length = 0
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1

        return length



if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLastWord("Hello World"))  # Output: 5
    print(sol.lengthOfLastWord("   fly me   to   the moon  "))  # Output: 4

    sol2 = SolutionTwo()
    print(sol2.lengthOfLastWord("Hello World"))  # Output: 5
    print(sol2.lengthOfLastWord("   fly me   to   the moon  "))  # Output: 4