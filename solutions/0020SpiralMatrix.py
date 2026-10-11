"""
LeetCode #54 - Spiral Matrix
Difficulty: Medium
Topics: Array, Matrix, Simulation
Date: 2026-10-11
Time spent: 45 min
Status: Solved

## Problem Statement
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Constraints:
- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 10
- -100 <= matrix[i][j] <= 100

## Idea
Maintain four boundaries (top, bottom, left, right). In each loop iteration,
traverse four edges in order: left→right (top row), top→bottom (right col),
right→left (bottom row), bottom→top (left col). After each edge, shrink
the corresponding boundary and check if boundaries cross (to avoid double-
counting when only one row/col remains).

## Complexity
- Time: O(m * n) — visit every element once
- Space: O(1) — only boundary variables (excluding output list)

## Submission Log
- [x] Submitted on LeetCode
- [x] Passed all test cases
"""


# ============================================================
# LeetCode Submission (copy entire block to LeetCode)
# ============================================================

class Solution(object):
    def spiralOrder(self, matrix):
        result = []
        m = len(matrix)        # 行数 = 外层列表长度
        n = len(matrix[0])     # 列数 = 第一行的长度
        top    = 0           # 上边界
        bottom = m - 1       # 下边界
        left   = 0           # 左边界
        right  = n - 1       # 右边界
        while len(result) < m * n:
            for j in range(left, right + 1):
                result.append(matrix[top][j])
            top += 1
            if top > bottom: break

            for j in range(top, bottom + 1):
                result.append(matrix[j][right])
            right -= 1
            if left > right: break

            for j in range(right, left - 1, -1):
                result.append(matrix[bottom][j])
            bottom -= 1
            if top > bottom: break

            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
        return result


# ============================================================
# 方法二：削皮算法（更简洁，但面试不推荐）
# 循环：(1) 收集第一行 (2) 去除第一行 (3) 逆时针旋转矩阵
# ============================================================

class Solution2(object):
    def spiralOrder(self, matrix):
        res = []
        while matrix:
            res.extend(matrix[0])               # (1) 收集第一行
            matrix.pop(0)                        # (2) 去除第一行
            matrix = list(zip(*matrix))[::-1]    # (3) 逆时针旋转
        return res

   