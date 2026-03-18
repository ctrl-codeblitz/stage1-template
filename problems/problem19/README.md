Problem: You are given a sorted array of integers (which may include negatives). Square each number in the array, then return the array sorted from smallest to largest.
Input: An integer array nums sorted in non-decreasing order 
Output: An integer array — the squared values sorted in non-decreasing order 
Example: nums = [-4, -1, 0, 3, 10] → [0, 1, 9, 16, 100] 
Time: O(n log n) — squaring is O(n), sorting is O(n log n) 
Space: O(n) — new array to store the squared values