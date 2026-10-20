"""
LeetCode #50 - Pow(x, n)
Difficulty: Medium
Topics: Math, Recursion, Binary Search
Date: 2026-10-20
Time spent: 40 min
Status: Solved

## Problem Statement
Implement pow(x, n), which calculates x raised to the power n.

Example 1:
Input: x = 2.00000, n = 10
Output: 1024.00000

Example 2:
Input: x = 2.10000, n = 3
Output: 9.26100

Example 3:
Input: x = 2.00000, n = -2
Output: 0.25000

## Idea
Fast exponentiation (快速幂). Use abs(n) to loop, keep reciprocal at the end.
While n > 0: if n is odd, multiply result by x; always square x; halve n.
This works because binary representation of n tells us which powers of x to multiply.
Key insight: take reciprocal (1/result) only at the end, not at the beginning,
to avoid floating-point error accumulation through repeated squaring.

## Complexity
- Time: O(log n) — n is halved each iteration
- Space: O(1) — only a few variables

## Submission Log
- [x] Submitted on LeetCode
- [x] Passed all test cases
"""


# ============================================================
# LeetCode Submission (copy entire block to LeetCode)
# ============================================================

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        result = 1
        m = abs(n)
        while m>0:
            if m % 2 !=0:
                result *= x
            x *= x
            m = m//2
        return result if n > 0 else 1/result
            

