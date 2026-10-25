"""
LeetCode #144 - Binary Tree Preorder Traversal
Difficulty: Easy
Topics: Binary Tree, DFS, Stack
Date: 2026-10-25
Time spent: 25 min
Status: Solved

## Problem Statement
Given the root of a binary tree, return the preorder traversal of its
nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [1,2,3]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]

## Idea
Recursive DFS with nested helper function. Outer function creates result
list, inner dfs() appends root.val then recurses left then right.
Base case: if node is None, return. All calls share the same result list.

## Complexity
- Time: O(n) — visit each node once
- Space: O(h) — recursion stack depth = tree height (O(n) worst case for skewed tree)

## Submission Log
- [x] Submitted on LeetCode
- [x] Passed all test cases
"""


# ============================================================
# LeetCode Submission (copy entire block to LeetCode)
# ============================================================

class Solution(object):
    def preorderTraversal(self, root):
        result = []                    # ← 只建一次
        def dfs(node):                 # ← 嵌套函数，共享 result
            if not node:
                return
            result.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)                      # ← 启动递归
        return result

        
