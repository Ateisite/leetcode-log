"""
LeetCode #1502 - Can Make Arithmetic Progression From Sequence
Difficulty: Easy
Topics: Array, Sorting
Date: 2026-09-30
Time spent: 20 min
Status: Solved

## Problem Statement
A sequence of numbers is called an arithmetic progression if the difference
between any two consecutive elements is the same.

Given an array of numbers arr, return true if the array can be rearranged
to form an arithmetic progression. Otherwise, return false.

Example 1:
Input: arr = [3,5,1]
Output: true
Explanation: We can reorder the elements as [1,3,5] or [5,3,1] with
differences 2 and -2 respectively, between each consecutive elements.

Example 2:
Input: arr = [1,2,4]
Output: false
Explanation: There is no way to reorder the elements to obtain an arithmetic
progression.

## Idea
Sort the array first. Calculate the common difference d from the first two
elements. Then iterate through all consecutive pairs: if any pair's
difference is not equal to d, return False. If the loop finishes without
finding a mismatch, return True.

## Complexity
- Time: O(n log n) due to sorting
- Space: O(1) sort is in-place

## Submission Log
- [x] Submitted on LeetCode
- [x] Passed all test cases
"""


# ============================================================
# LeetCode Submission (copy entire block to LeetCode)
# ============================================================

class Solution(object):
    def canMakeArithmeticProgression(self, arr):
       arr.sort()
       d = arr[1] - arr[0]
       for i in range(len(arr)-1):
           if arr[i+1]-arr[i] != d:
               return False
       return True
