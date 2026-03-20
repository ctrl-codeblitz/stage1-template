# Problem 4 - Append Words Without Duplicates

Given an initial message and a list of words to append, append each word only
if it does not already exist in the current message.

## Input Format

- First line: the initial message string (space-separated words).
- Second line: space-separated words to append in order.

## Output Format

A single line string: the final message after appending only missing words.

## Example

Input:
hello world
world friend hi

Output:
hello world friend hi

## Constraints

- Word matching is exact and case-sensitive.

## Expected Complexity

- Time: O(m + n) with a hash set
- Space: O(k) for unique words
