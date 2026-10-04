"""
LeetCode #709 - To Lower Case
Difficulty: Easy
Topics: String
Date: 2026-10-04
Time spent: 25 min
Status: Solved

## Problem Statement
Given a string s, return the string after replacing every uppercase letter
with the same lowercase letter.

Example 1:
Input: s = "Hello"
Output: "hello"

Example 2:
Input: s = "here"
Output: "here"

Example 3:
Input: s = "LOVELY"
Output: "lovely"

## Idea
Traverse each character in the string. If the character is an uppercase
letter ('A' <= c <= 'Z'), convert it to lowercase by adding 32 to its
ASCII code (chr(ord(c) + 32)). Otherwise keep the character unchanged.
Build and return the result string.

## Complexity
- Time: O(n) single pass through the string
- Space: O(n) for the result string

## Submission Log
- [x] Submitted on LeetCode
- [x] Passed all test cases
"""


# ============================================================
# LeetCode Submission (copy entire block to LeetCode)
# ============================================================

class Solution(object):
    def toLowerCase(self, s):
        result = ""
        for c in s:
            if 'A' <= c <= 'Z': 
                result = result + chr(ord(c)+32)
            else:
                result = result + c 
        return result
