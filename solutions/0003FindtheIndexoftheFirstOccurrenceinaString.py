"""
LeetCode #28 - Find the Index of the First Occurrence in a String
Difficulty: Easy
Topics: String, Two Pointers
Date: 2026-09-24
Time spent: 20 min
Status: Solved

## Problem Statement
Given two strings needle and haystack, return the index of the first
occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.

Constraints:
1 <= haystack.length, needle.length <= 10^4
haystack and needle consist of only lowercase English characters.

## Idea
Use Python's built-in str.find() method, which returns the index of the first
occurrence of a substring, or -1 if not found. This is the simplest approach.

(Manual approach: iterate through haystack and compare slices of length
len(needle) with needle.)

## Complexity
- Time: O(n*m) where n = len(haystack), m = len(needle)
- Space: O(1)

## Submission Log
- [x] Submitted on LeetCode
- [x] Passed all test cases
"""


# ============================================================
# LeetCode Submission (copy entire block to LeetCode)
# ============================================================

class Solution(object):
    def strStr(self, haystack, needle):
        return haystack.find(needle)
