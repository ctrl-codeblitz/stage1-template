Append to a message, but no duplicates

Problem: Given an initial message (string) and a list of words to append, append each word if it is not already present in the message (matching exact words). Words are space-separated. Return the final message.

Input: first line: initial message; second line: space-separated words to append
Output: final message
Example: initial: "hello world", append: "world friend hi" → "hello world friend hi"
Time: O(m + n) if using a hash set, Space: O(k) where k = unique words
