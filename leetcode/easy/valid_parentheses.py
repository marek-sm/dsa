"""
Problem: Valid Parentheses (LeetCode #20, Easy)
Link: https://leetcode.com/problems/valid-parentheses/
Category: String / Stack

Thoughts:
- Initially knew to use a dictionary to store the three types of brackets as pairs.
- Realized that I could use a stack to keep track of opening brackets and ensure they match with closing ones.
- As I iterated through the string in an index-based manner, I would push opening brackets onto the stack.
- When encountering a closing bracket, I would check if the stack is not empty and if the top of the stack matches the corresponding opening bracket.
- If they match, I would pop the top of the stack; if not, I would return False.
- At the end of the iteration, if the stack is empty, it means all brackets were matched correctly, and I would return True; otherwise, I would return False.
- After, I found a similar solution that iterates through the string directly, which is slightly faster because it avoids index lookups and less memory usage because it does not use the range function.

Approach:

Solution 1 (Stack-based Parenthesis Validation (index-based)) - my solution: 
- Use a stack to track opening parentheses and ensure they match with closing ones.

Solution 2 (Stack-based Parenthesis Matching) - not my solution
- Similar to Solution 1 but uses direct character iteration for clarity.
"""

# -----------------------------
# Solution 1: Stack-based Parenthesis Validation (index-based) - my solution
# Time Complexity: O(N), Space Complexity: O(N)
# -----------------------------
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {")":"(", "}":"{", "]":"["}
        for i in range(len(s)):
            if s[i] not in pairs:
                stack.append(s[i])
            else:
                if stack and stack[-1] == pairs[s[i]]:
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        else:
            return False

# -----------------------------
# Solution 2: Stack-based Parenthesis Matching - not my solution
# Time Complexity: O(N), Space Complexity: O(N)
# -----------------------------
class SolutionTwo:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {")": "(", "}": "{", "]": "["}
        for ch in s:
            if ch in pairs.values():      # opening bracket
                stack.append(ch)
            elif ch in pairs:             # closing bracket
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            else:
                return False              # invalid character (optional)
        return not stack




if __name__ == "__main__":
    sol = Solution()
    print(sol.isValid("()"))          # Output: True
    print(sol.isValid("()[]{}"))      # Output: True
    print(sol.isValid("(]"))          # Output: False

    sol2 = SolutionTwo()
    print(sol2.isValid("()"))          # Output: True
    print(sol2.isValid("()[]{}"))      # Output: True
    print(sol2.isValid("(]"))          # Output: False