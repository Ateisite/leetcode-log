"""
LeetCode #1523 - Count Odd Numbers in an Interval Range
Difficulty: Easy
Topics: Math
Date: 2026-10-13
Time spent: 10 min
Status: Solved

## Problem Statement
Given two non-negative integers low and high. Return the count of odd
numbers between low and high (inclusive).

Example 1:
Input: low = 3, high = 7
Output: 3
Explanation: The odd numbers between 3 and 7 are [3,5,7].

Example 2:
Input: low = 8, high = 10
Output: 1
Explanation: The odd numbers between 8 and 10 are [9].

## Idea
Total numbers in range = high - low + 1. Half of them are odd (integer
division). If both endpoints are odd, there's one extra odd number.

## Complexity
- Time: O(1) — pure math calculation
- Space: O(1)

## Submission Log
- [x] Submitted on LeetCode
- [x] Passed all test cases
"""


# ============================================================
# LeetCode Submission (copy entire block to LeetCode)
# ============================================================

class Solution(object):
    def countOdds(self, low, high):
        s = (high-low+1)//2
        if low % 2 != 0 and high % 2 != 0:
            s = s +1
        return s