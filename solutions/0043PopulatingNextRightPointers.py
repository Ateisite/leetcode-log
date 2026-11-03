"""
LeetCode #116 - Populating Next Right Pointers in Each Node
Difficulty: Medium
Topics: Binary Tree, BFS, Linked List
Date: 2026-11-03
Time spent: 25 min
Status: Solved

## Problem Statement
Given a perfect binary tree (all leaves are on the same level, and every
parent has two children), populate each next pointer to point to its next
right node. If there is no next right node, the next pointer should be
set to NULL.

Example 1:
Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]

Example 2:
Input: root = []
Output: []

## Idea
层序遍历，每层从左到右把节点存到 level 列表，
然后 for i in range(len(level)-1): level[i].next = level[i+1]。
最后一个节点的 next 默认就是 None，不用手动设。

## Complexity
- Time: O(n) — 每个节点访问一次
- Space: O(n) — 队列 + level 列表

## Submission Log
- [x] Submitted on LeetCode (2026-11-03)
- [x] Passed all test cases
"""


# ============================================================
# LeetCode Submission (copy entire block to LeetCode)
# ============================================================
# 题目：完美二叉树，每个节点的 next 指针指向同层右边的节点
# 思路：层序遍历，每层从左到右，前一个节点的 next 指向当前节点
# 易错点：
#   - 每层第一个节点没有前一个，next 保持 None
#   - 每层最后一个节点的 next 也是 None
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
            level =[]
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
