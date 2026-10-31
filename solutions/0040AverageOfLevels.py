"""
LeetCode #637 - Average of Levels in Binary Tree
Difficulty: Easy
Topics: Binary Tree, BFS
Date: 2026-10-31
Time spent: 15 min
Status: Solved

## Problem Statement
Given the root of a binary tree, return the average value of the nodes
on each level.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [3.00000, 14.50000, 11.00000]

Example 2:
Input: root = [3,9,20,15,7]
Output: [3.00000, 14.50000, 11.00000]

## Idea
层序遍历，每层求平均：sum(level) / len(level)。

## Complexity
- Time: O(n) — 每个节点访问一次
- Space: O(n) — 队列 + 结果

## Submission Log
- [x] Submitted on LeetCode (2026-10-31)
- [x] Passed all test cases
"""


# ============================================================
# LeetCode Submission (copy entire block to LeetCode)
# ============================================================
# 题目：每层节点的平均值
# 思路：层序遍历，每层求和后除以节点数：sum(level) / len(level)
# 易错点：
#   - Python 3 中 / 自动返回浮点数，不需要转 float
#   - 空树返回 []

from collections import deque
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[float]
        """
        result = []
        if not root:
            return result
        queue = deque()
        queue.append(root)
        

        while queue:
            level = []
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            average = sum(level)/len(level)
            result.append(average)
        return result
