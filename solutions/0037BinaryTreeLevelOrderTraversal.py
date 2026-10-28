"""
LeetCode #102 - Binary Tree Level Order Traversal
Difficulty: Medium
Topics: Binary Tree, BFS, Queue
Date: 2026-10-28
Time spent: 40 min
Status: Solved

## Problem Statement
Given the root of a binary tree, return the level order traversal of its
nodes' values. (i.e., from left to right, level by level).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []

## Idea
BFS 用队列（collections.deque）。每次处理一整层：
- 记录当前层节点数 size，for size 次弹出并记录值
- 每个节点的左右孩子入队，作为下一层
- 每层的结果追加到 result，最终返回二维列表

## Complexity
- Time: O(n) — 每个节点访问一次
- Space: O(n) — 队列最多容纳一层的节点数（最宽那层）

## Submission Log
- [x] Submitted on LeetCode (2026-10-28)
- [x] Passed all test cases
"""


# ============================================================
# LeetCode Submission (copy entire block to LeetCode)
# ============================================================
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
        return result

        
