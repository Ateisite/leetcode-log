"""
LeetCode #58 - Length of Last Word
Difficulty: Easy
Topics: String
Date: 2026-10-03
Time spent: 10 min
Status: Solved

## Problem Statement
Given a string s consisting of words and spaces, return the length of the
last word in the string.

A word is a maximal substring consisting of non-space characters only.

Example 1:
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.

## Idea
Use Python's built-in split() method to split the string by spaces into a
list of words. Then take the last element with [-1] and return its length.

## Complexity
- Time: O(n) split traverses the string once
- Space: O(n) for the list of words

## Submission Log
- [x] Submitted on LeetCode
- [x] Passed all test cases
"""


# ============================================================
# LeetCode Submission (copy entire block to LeetCode)
# ============================================================

class Solution(object):
    def lengthOfLastWord(self, s):
        words = s.split()
        last = words[-1]
        return len(last)
