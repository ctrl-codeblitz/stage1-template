Power (x^n) — recursive

Stage: 2 (Recursive)
Problem: Given base x and non-negative integer exponent n, compute x^n recursively.
Hint: x^n = x * x^(n-1) for n > 0; x^0 = 1. (For efficiency, use x^n = (x^(n/2))^2 when n is even.)

Input: two integers x and n (one per line or space-separated)
Output: one integer — x^n (assume result fits in int/long)
Example: x=2, n=10 → 1024
Time: O(n) naive or O(log n) with squaring, Space: O(log n) recursion
