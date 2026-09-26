"""
LeetCode #459 - Repeated Substring Pattern
Difficulty: Easy
Topics: String
Date: 2026-09-26
Time spent: 25 min
Status: Solved

## Problem Statement
Given a string s, check if it can be constructed by taking a substring of
it and appending multiple copies of the substring together.

Example 1:
Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.

Example 2:
Input: s = "aba"
Output: false

Example 3:
Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring "abcabc"
twice.

## Idea
Enumerate all possible substring lengths i (from 1 to len(s)-1). If i is
a divisor of len(s), take the prefix s[:i] and repeat it len(s)//i times.
If the result equals the original string s, return True. If no divisor
works, return False.

## Complexity
- Time: O(n * d) where d = number of divisors of n
- Space: O(n) for the repeated string

## Submission Log
- [x] Submitted on LeetCode
- [x] Passed all test cases
"""


# ============================================================
# LeetCode Submission (copy entire block to LeetCode)
# ============================================================

class Solution(object):
    def repeatedSubstringPattern(self, s):
        for i in range(1,len(s)):
            if len(s) % i == 0:
                sub = s[:i]
                times = len(s) // i
                if sub*times == s:
                    return True
        return False
            