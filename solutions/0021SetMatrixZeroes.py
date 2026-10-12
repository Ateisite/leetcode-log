"""
LeetCode #73 - Set Matrix Zeroes
Difficulty: Medium
Topics: Array, Matrix
Date: 2026-10-12
Time spent: 20 min
Status: Solved

## Problem Statement
Given an m x n integer matrix, if an element is 0, set its entire row and
column to 0's. Must do it in-place.

Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

## Idea
Two-pass approach. First pass: scan the matrix, record which rows and
columns contain 0 (using sets). Second pass: set cell to 0 if its row or
column is in the recorded sets. This avoids the problem of 0's spreading
during iteration.

## Complexity
- Time: O(m * n) — two passes through the matrix
- Space: O(m + n) — sets store row and column indices

## Submission Log
- [x] Submitted on LeetCode
- [x] Passed all test cases
"""


# ============================================================
# LeetCode Submission (copy entire block to LeetCode)
# ============================================================

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        rows = set()
        cols = set()

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        for i in range(m):
            for j in range(n):
                if i in rows or j in cols:
                    matrix[i][j] = 0
