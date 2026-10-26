"""
LeetCode #145 - Binary Tree Postorder Traversal
Difficulty: Easy
Topics: Binary Tree, DFS, Stack
Date: 2026-10-26
Time spent: 15 min
Status: Solved

## Problem Statement
Given the root of a binary tree, return the postorder traversal of its
nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [3,2,1]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]

## Idea
DFS 递归，后序遍历 = 左右根。
用嵌套函数 dfs 共享外层的 result 列表：
- 递归左子树 → 递归右子树 → 把根的值 append 到 result
- 基准条件：if not root: return

## Complexity
- Time: O(n) — 每个节点访问一次
- Space: O(n) — 递归栈深度最坏情况（链状树）

## Submission Log
- [x] Submitted on LeetCode (2026-10-26)
- [x] Passed all test cases
"""


# ============================================================
# LeetCode Submission (copy entire block to LeetCode)
# ============================================================

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            dfs(root.right)
            result.append(root.val)
            
        dfs(root)
        return result