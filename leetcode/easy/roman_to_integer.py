"""
Problem: Roman to Integer (LeetCode #13, Easy)
Link: https://leetcode.com/problems/roman-to-integer/
Category: Hash Table / Math / String

Thoughts:
- Saw that each symbol had a corresponding integer value that could be easily mapped using a dictionary.
- I could then iterate through the string, add the corresponding values of each symbol.
- However, this was complicated by some two symbols acting as a single one to represent a different value.
- I realized that I could simply subtract double the amount of the first symbol for each time it happened.
- This worked because the two symbol combination value was always the value of the first symbol subtracted from the second.
- After submitting, I was not happy with my runtime latency, so I searched for a better solution.
- While the listed optimal solution is still O(n) time complexity, it is more efficient as it only requires one pass through the string instead of two, and it uses less slicing.
- My solution and the optimal solution are the same with regard to space complexity, both being O(1) as the dictionary size is constant.

Approach:

Solution 1 (Two-Pass with Adjustments) - my solution: 
- Add all Roman numeral values.
- In a second loop, subtract corrections for special subtractive cases (IV, IX, XL, XC, CD, CM).

Solution 2 (One-Pass Optimal) - not my solution:
- Traverse the string once.
- If the current numeral is smaller than the next numeral, subtract it, if not, add it.
- This naturally handles all subtractive cases without explicit checks.
"""

# -----------------------------
# Solution 1: Two-Pass with Adjustments - my solution
# Time Complexity: O(N)
# Space Complexity: O(1)
# -----------------------------
class Solution:
    def romanToInt(self, s: str) -> int:
        number = 0
        conversions = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }

        for symbol in s:
            number += conversions[symbol]
        
        for i in range(len(s) - 1):
            if s[i:i+2] == "IV" or s[i:i+2] == "IX":
                number -= 2
            elif s[i:i+2] == "XL" or s[i:i+2] == "XC":
                number -= 20
            elif s[i:i+2] == "CD" or s[i:i+2] == "CM":
                number -= 200
    
        return number

# -----------------------------
# Solution 2: One-Pass Optimal - not my solution
# Time Complexity: O(N)
# Space Complexity: O(1)
# -----------------------------
class SolutionOnePass:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        
        result = 0
        n = len(s)
        for i in range(n):
            curr = roman[s[i]]
            if i + 1 < n and curr < roman[s[i+1]]:
                result -= curr
            else:
                result += curr
        return result



if __name__ == "__main__":
    sol = Solution()
    print(sol.romanToInt("III"))      # 3
    print(sol.romanToInt("IV"))       # 4
    print(sol.romanToInt("IX"))       # 9
    print(sol.romanToInt("LVIII"))    # 58
    print(sol.romanToInt("MCMXCIV"))  # 1994

    sol_one_pass = SolutionOnePass()
    print(sol_one_pass.romanToInt("III"))      # 3
    print(sol_one_pass.romanToInt("IV"))       # 4
    print(sol_one_pass.romanToInt("IX"))       # 9
    print(sol_one_pass.romanToInt("LVIII"))    # 58
    print(sol_one_pass.romanToInt("MCMXCIV"))  # 1994