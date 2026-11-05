"""
LeetCode #104 - Maximum Depth of Binary Tree
Difficulty: Easy
Topics: Binary Tree, DFS, BFS
Date: 2026-11-05
Time spent: 20 min
Status: Solved

## Problem Statement
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest
path from the root node down to the farthest leaf node.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2

## Idea
DFS 递归：最大深度 = max(左子树深度, 右子树深度) + 1
基准：空节点返回 0

## Complexity
- Time: O(n) — 每个节点访问一次
- Space: O(n) — 递归栈深度（链状树最坏）

## Submission Log
- [x] Submitted on LeetCode (2026-11-05)
- [x] Passed all test cases
"""


# ============================================================
# LeetCode Submission (copy entire block to LeetCode)
# ============================================================
# 题目：二叉树的最大深度
# 思路：递归，最大深度 = max(左子树深度, 右子树深度) + 1
# 易错点：
#   - 基准条件：if not root: return 0
#   - 记得 +1（当前层）

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        
        if not root:
            return 0
        return max(self.maxDepth(root.left),self.maxDepth(root.right))+1
        


