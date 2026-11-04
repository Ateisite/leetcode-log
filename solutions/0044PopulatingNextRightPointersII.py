"""
LeetCode #117 - Populating Next Right Pointers in Each Node II
Difficulty: Medium
Topics: Binary Tree, BFS
Date: 2026-11-04
Time spent: 5 min
Status: Solved

## Problem Statement
Given a binary tree (not necessarily perfect), populate each next pointer
to point to its next right node. If there is no next right node, the next
pointer should be set to NULL.

Example 1:
Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]

Example 2:
Input: root = []
Output: []

## Idea
和 #116 一样：层序遍历 + 同层连接。普通二叉树可能缺节点，但 if left/right 已经处理了。

## Complexity
- Time: O(n) — 每个节点访问一次
- Space: O(n) — 队列 + level 列表

## Submission Log
- [x] Submitted on LeetCode (2026-11-04)
- [x] Passed all test cases
"""


# ============================================================
# LeetCode Submission (copy entire block to LeetCode)
# ============================================================
# 题目：普通二叉树（不一定完美），每个节点的 next 指向同层右边的节点
# 思路：和 #116 一样，层序遍历 + 同层连接
# 易错点：
#   - level 存节点，不是值
#   - 普通二叉树可能缺节点，但 if node.left/right 已经处理了
from collections import deque
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root
        queue = deque()
        queue.append(root)

        while queue:
            level = []
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                level.append(node)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            for i in range(len(level)-1):
                level[i].next = level[i+1]
        return root
