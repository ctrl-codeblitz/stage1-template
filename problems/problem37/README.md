Decimal to binary — recursive

Stage: 2 (Recursive)
Problem: Convert a non-negative decimal integer to its binary representation using recursion.
Hint: n in binary = (n/2 in binary) concatenated with (n%2). Base case: 0 → "0".

Input: one non-negative integer n
Output: binary string (e.g. no leading zeros, or with leading zeros for fixed width — state in problem)
Example: 12 → 1100
Time: O(log n), Space: O(log n) recursion
