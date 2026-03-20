# Problem 19 - Square and Sort Array

Given a sorted integer array (possibly including negatives), square each value
and return the squared values in non-decreasing order.

## Input Format

A single line containing a bracketed list literal of integers,
for example [-10, -7, -5, -2, -1].

## Output Format

A bracketed list literal of squared integers in non-decreasing order.

## Example

Input:
[-3, -1, 0, 1, 3]

Output:
[0, 1, 1, 9, 9]

## Constraints

- Input list is already sorted in non-decreasing order.

## Expected Complexity

- Time: O(n log n) for square-then-sort baseline
- Space: O(n)