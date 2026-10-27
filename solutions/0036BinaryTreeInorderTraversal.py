"""
LeetCode #94 - Binary Tree Inorder Traversal
Difficulty: Easy
Topics: Binary Tree, DFS, Stack
Date: 2026-10-27
Time spent: 10 min
Status: Solved

## Problem Statement
Given the root of a binary tree, return the inorder traversal of its
nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]

## Idea
DFS 递归，中序遍历 = 左→根→右。
嵌套函数 dfs 共享外层 result：
- 递归左子树 → append 根 → 递归右子树
- 基准：if not root: return
与前序/后序同一模板，仅 append 位置不同。

## Complexity
- Time: O(n) — 每个节点访问一次
- Space: O(n) — 递归栈深度（链状树最坏）

## Submission Log
- [x] Submitted on LeetCode (2026-10-27)
- [x] Passed all test cases
"""


# ============================================================
# LeetCode Submission (copy entire block to LeetCode)
# ============================================================

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []
        def dfs(head):
            if not head:
                return
            dfs(head.left)
            result.append(head.val)
            dfs(head.right)
        dfs(root)
        return result

