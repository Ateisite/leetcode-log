"""
LeetCode #107 - Binary Tree Level Order Traversal II
Difficulty: Medium
Topics: Binary Tree, BFS, Queue
Date: 2026-10-30
Time spent: 15 min
Status: Solved

## Problem Statement
Given the root of a binary tree, return the bottom-up level order traversal
of its nodes' values. (i.e., from left to right, level by level from leaf to root).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[15,7],[9,20],[3]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []

## Idea
#102 层序遍历 + result.reverse()。BFS 从上到下遍历，最后反转结果即可。

## Complexity
- Time: O(n) — 每个节点访问一次
- Space: O(n) — 队列 + 结果

## Submission Log
- [x] Submitted on LeetCode (2026-10-30)
- [x] Passed all test cases
"""


# ============================================================
# LeetCode Submission (copy entire block to LeetCode)
# ============================================================
# 题目：层序遍历，但结果从下到上（叶子层在前，根层在最后）
# 思路：#102 层序遍历 + 最后反转结果（result.reverse() 或 result[::-1]）
# 易错点：
#   - deque([root]) 要加中括号
#   - popleft() 不是 pop()
#   - size = len(queue) 在 for 外记录

from collections import deque
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
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
            result.append(level)
        result.reverse()
        return result