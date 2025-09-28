"""
Problem: Longest Common Prefix (LeetCode #14, Easy)
Link: https://leetcode.com/problems/longest-common-prefix/
Category: Array / String / Trie

Thoughts:
- Saw how I should iterate through each word in the list and compare characters.
- Realized that the maximum amount of times I would need to iterate through the words is the length of the smallest word minus one
- I could then build the common prefix string character by character until a mismatch is found.
- As soon as this happens, I could return the string as built so far.
- After submitting, I realized that I needed to adjust for lists with one or less strings, as the j variable would be undefined.

Approach:
- Find the length of the shortest string in the list.
- Iterate through each character index up to the length of the shortest string.
- For each character index, compare the character in each string.
- If all characters match, append to the result string.
- If a mismatch is found, return the result string immediately.
- If no mismatches are found, return the result string after the loop.

Time Complexity: O(M*N) because I iterate through M characters for N strings
Space Complexity: O(1) as I use a constant amount of variables
"""

from typing import List

# -----------------------------
# Solution: Vertical Scanning - my solution
# Time Complexity: O(M*N), Space Complexity: O(1)
# -----------------------------
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) < 2:
            return strs[0]
        shortest = len(min(strs))
        finalString = ""
        for i in range(shortest):
            for j in range(len(strs) - 1):
                if strs[j][i] != strs[j+1][i]:  
                    return finalString
            finalString += strs[j][i]
        return finalString

if __name__ == "__main__":
    sol = Solution()
    print(sol.longestCommonPrefix(["flower","flow","flight"]))  # Output: "fl"
    print(sol.longestCommonPrefix(["dog","racecar","car"]))     # Output: ""