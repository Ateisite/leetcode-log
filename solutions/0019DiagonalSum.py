"""
LeetCode #1572 - Diagonal Sum
Difficulty: Easy
Topics: Array, Matrix
Date: 2026-10-10
Time spent: 25 min
Status: Solved

## Problem Statement
给你一个正方形矩阵 mat，请你返回矩阵对角线元素的和。
返回在矩阵主对角线上的元素和副对角线上且不在主对角线上元素的和。

示例 1：
输入：mat = [[1,2,3],
            [4,5,6],
            [7,8,9]]
输出：25
解释：对角线的和为：1 + 5 + 9 + 3 + 7 = 25
请注意，元素 mat[1][1] = 5 只会被计算一次。

示例 2：
输入：mat = [[1,1,1,1],
            [1,1,1,1],
            [1,1,1,1],
            [1,1,1,1]]
输出：8

示例 3：
输入：mat = [[5]]
输出：5

## Idea
Loop through each row i, add both mat[i][i] (main diagonal) and
mat[i][n-1-i] (anti-diagonal). If n is odd, the center element was
counted twice, so subtract it once.

## Complexity
- Time: O(n) — single pass through n rows
- Space: O(1) — only use a scalar variable

## Submission Log
- [x] Submitted on LeetCode
- [x] Passed all test cases
"""


# ============================================================
# LeetCode Submission (copy entire block to LeetCode)
# ============================================================

class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        total = 0
        for i in range(len(mat)):
            total += mat[i][i] + mat[i][len(mat)-i-1]
        if len(mat)%2 == 0:
            return total
        else:
            return total-mat[len(mat)//2][len(mat)//2]