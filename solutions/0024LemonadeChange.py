"""
LeetCode #860 - Lemonade Change
Difficulty: Easy
Topics: Array, Greedy
Date: 2026-10-16
Time spent: 20 min
Status: Solved

## Problem Statement
At a lemonade stand, each lemonade costs $5. Customers pay with $5, $10,
or $20 bills. You must provide correct change. Return true if you can
give every customer correct change, false otherwise.

Example 1:
Input: bills = [5,5,5,10,20]
Output: true

Example 2:
Input: bills = [5,5,10,10,20]
Output: false

## Idea
Greedy approach. Track count of $5 and $10 bills. For each customer:
- $5: no change needed
- $10: need one $5
- $20: prefer giving $10+$5 (saves $5 for future), else give 3x$5.
Return False immediately if change cannot be made.

## Complexity
- Time: O(n) — single pass through bills
- Space: O(1) — only two counter variables

## Submission Log
- [x] Submitted on LeetCode
- [x] Passed all test cases
"""


# ============================================================
# LeetCode Submission (copy entire block to LeetCode)
# ============================================================

class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        count_5 = 0
        count_10 = 0
        for i in bills:
            if i == 5:
                count_5 += 1
            if i == 10:
                if count_5 != 0:
                    count_5 -= 1
                    count_10 += 1
                else :
                    return False
            if i == 20:
                if count_10 != 0 and count_5 != 0:
                    count_5 -= 1
                    count_10 -= 1
                elif count_10 == 0 and count_5 >= 3:
                    count_5 -= 3
                else :
                    return  False
        return True

