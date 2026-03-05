GCD (Greatest Common Divisor) — recursive

Stage: 2 (Recursive)
Problem: Implement the GCD of two non-negative integers using Euclid's algorithm recursively.
Hint: gcd(a, b) = gcd(b, a % b) when b ≠ 0, else gcd(a, 0) = a.

Input: two integers a and b (one per line or space-separated)
Output: one integer — gcd(a, b)
Example: a=48, b=18 → 6
Time: O(log min(a,b)), Space: O(log min(a,b)) for recursion
