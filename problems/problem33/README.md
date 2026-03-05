Sum of digits — recursive

Stage: 2 (Recursive)
Problem: Given a non-negative integer (e.g. 1234), compute the sum of its decimal digits using recursion.
Hint: sum_digits(n) = n % 10 + sum_digits(n / 10), base case when n == 0.

Input: one integer n (e.g. 1234)
Output: one integer — sum of digits
Example: 1234 → 10
Time: O(digits), Space: O(digits) for recursion
