"""
LeetCode #1491 - Average Salary Excluding the Minimum and Maximum Salary
Difficulty: Easy
Topics: Array, Sorting
Date: 2026-10-15
Time spent: 10 min
Status: Solved

## Problem Statement
Given an array of unique integers salary, return the average salary
excluding the minimum and maximum salary.

Example 1:
Input: salary = [4000,3000,1000,2000]
Output: 2500.00000

Example 2:
Input: salary = [1000,2000,3000]
Output: 2000.00000

## Idea
Use built-in sum(), min(), max() to compute total salary excluding
min and max. Divide by count (len - 2) with float conversion to ensure
floating-point result.

## Complexity
- Time: O(n) — single pass for sum, min, max
- Space: O(1)

## Submission Log
- [x] Submitted on LeetCode
- [x] Passed all test cases
"""


# ============================================================
# LeetCode Submission (copy entire block to LeetCode)
# ============================================================

class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        total = sum(salary)-min(salary)-max(salary)
        count = len(salary)-2
        return total/float(count)