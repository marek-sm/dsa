"""
Problem: Fibonacci Number (LeetCode #509, Easy)
Link: https://leetcode.com/problems/fibonacci-number/
Category: Math / Dynamic Programming / Recursion / Memoization

Thoughts:
- I initially wrote the recursive approach, which is the most straightforward way to define the Fibonacci sequence.
- However, I realized that this approach has an exponential time complexity due to the repeated calculations of the same Fibonacci numbers.
- To optimize the solution, I instead wrote an iterative approach that simply uses a loop, avoiding the stack overhead of recursion.

Approach:

Solution 1 (Recursive version):
- Define the base cases for n = 0 and n = 1.
- For n > 1, return the sum of the Fibonacci of (n-1) and (n-2).
- This approach has a time complexity of O(2^N) due to the exponential growth of recursive calls, and a space complexity of O(N) due to the call stack.

Solution 2 (Iterative version):
- Handle the base cases for n = 0 and n = 1.
- Use two variables to keep track of the last two Fibonacci numbers.
- Iterate from 2 to n, updating the two variables to represent the next Fibonacci number.
- This approach has a time complexity of O(N) and a space complexity of O(1) since it only uses a constant amount of extra space.
"""

# -----------------------------
# Solution 1: Recursive version - my solution
# Time Complexity: O(2^N)
# Space Complexity: O(N)
# -----------------------------
class SolutionRecursive:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        else:
            return self.fib(n-1) + self.fib(n-2)  

# -----------------------------
# Solution 2: Iterative version - my solution
# Time Complexity: O(N)
# Space Complexity: O(1)
# -----------------------------
class SolutionIterative:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        a, b = 0, 1
        for _ in range (2, n + 1):
            a, b = b, a + b

        return b



if __name__ == "__main__":
    sol = SolutionRecursive()
    print("Recursive version: ")
    print(sol.fib(2))  # Output: 1
    print(sol.fib(5))  # Output: 5
    print(sol.fib(15)) # Output: 610

    print()

    sol2 = SolutionIterative()
    print("Iterative version:")
    print(sol2.fib(2))  # Output: 1
    print(sol2.fib(5))  # Output: 5
    print(sol2.fib(15)) # Output: 610