"""
LeetCode #1672 - Richest Customer Wealth
Difficulty: Easy
Topics: Array, Matrix
Date: 2026-10-08
Time spent: 20 min
Status: Solved

## Problem Statement
You are given an m x n integer grid accounts where accounts[i][j] is the
amount of money the ith customer has in the jth bank. Return the wealth
that the richest customer has.

A customer's wealth is the amount of money they have in all their bank
accounts. The richest customer is the customer that has the maximum wealth.

Example 1:
Input: accounts = [[1,2,3],[3,2,1]]
Output: 6
Explanation:
1st customer has wealth = 1 + 2 + 3 = 6
2nd customer has wealth = 3 + 2 + 1 = 6
Both customers are considered the richest with a wealth of each, so return 6.

Example 2:
Input: accounts = [[1,5],[7,3],[3,5]]
Output: 10
Explanation:
1st customer has wealth = 6
2nd customer has wealth = 10
3rd customer has wealth = 8
The 2nd customer is the richest with a wealth of 10.

Example 3:
Input: accounts = [[2,8,7],[7,1,3],[1,9,5]]
Output: 17

## Idea
Iterate through each customer (each row of the 2D grid). Use sum() to
calculate each customer's total wealth, and track the maximum with a
variable updated inside the loop.

## Complexity
- Time: O(m * n) — visit every element once (m customers, n banks each)
- Space: O(1) — only use two scalar variables

## Submission Log
- [x] Submitted on LeetCode
- [x] Passed all test cases
"""


# ============================================================
# LeetCode Submission (copy entire block to LeetCode)
# ============================================================

class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        max_wealth = 0
        for customer in accounts:
            total = sum(customer)
            if total > max_wealth:
                max_wealth = total
        return max_wealth
