All subsets — recursive

Stage: 2 (Recursive)
Problem: Given a set of distinct elements (e.g. {a, b, c, d, e, f}), output all subsets using recursion. Include/exclude each element and recurse.

Input: first line n (number of elements), second line n space-separated elements (single chars or words)
Output: 2^n lines — each line is one subset (space-separated elements). Empty set as an empty line. Order: any deterministic order (e.g. lexicographic).
Example: n=2, set "a b" → empty line, "a", "a b", "b" (four lines)
Time: O(2^n), Space: O(n) recursion
