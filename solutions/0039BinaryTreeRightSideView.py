"""
LeetCode #199 - Binary Tree Right Side View
Difficulty: Medium
Topics: Binary Tree, BFS, DFS
Date: 2026-10-31
Time spent: 10 min
Status: Solved

## Problem Statement
Given the root of a binary tree, imagine yourself standing on the right
side of it. Return the values of the nodes you can see ordered from top
to bottom.

Example 1:
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Example 2:
Input: root = [1,null,3]
Output: [1,3]

Example 3:
Input: root = []
Output: []

## Idea
层序遍历（BFS），每层处理完后只取最右边的值：result.append(level[-1])。

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
# 题目：站在二叉树右边看，能看到的节点值（从上到下）
# 思路：层序遍历，每层只取最后一个节点（最右边的）
# 易错点：
#   - 每层最后一个 = level[-1]
#   - 空树返回 []

from collections import deque
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
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
            result.append(level[-1])
        return result

                       
