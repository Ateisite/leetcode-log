"""
LeetCode #429 - N-ary Tree Level Order Traversal
Difficulty: Medium
Topics: Binary Tree, BFS, Queue
Date: 2026-11-01
Time spent: 10 min
Status: Solved

## Problem Statement
Given an n-ary tree, return the level order traversal of its nodes' values.

Example 1:
Input: root = [1,null,3,2,4,null,5,6]
Output: [[1],[3,2,4],[5,6]]

Example 2:
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]

## Idea
#102 层序遍历模板，把 if left/right 换成 for child in node.children。

## Complexity
- Time: O(n) — 每个节点访问一次
- Space: O(n) — 队列 + 结果

## Submission Log
- [x] Submitted on LeetCode (2026-11-01)
- [x] Passed all test cases
"""


# ============================================================
# LeetCode Submission (copy entire block to LeetCode)
# ============================================================
# 题目：N叉树的层序遍历（二叉树升级版）
# 思路：和 #102 一样，但节点有多个孩子，用 for child in node.children 遍历
# 易错点：
#   - N叉树节点用 node.children（列表），不是 node.left/right
#   - for child in node.children: queue.append(child)


from collections import deque
class Solution(object):
    def levelOrder(self, root):
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
                for child in node.children:
                    queue.append(child)
            result.append(level)
        return result
