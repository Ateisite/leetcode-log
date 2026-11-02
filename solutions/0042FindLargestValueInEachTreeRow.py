"""
LeetCode #515 - Find Largest Value in Each Tree Row
Difficulty: Medium
Topics: Binary Tree, BFS
Date: 2026-11-02
Time spent: 10 min
Status: Solved

## Problem Statement
Given the root of a binary tree, return an array of the largest value in each row.

Example 1:
Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]

Example 2:
Input: root = [1,2,3]
Output: [1,3]

## Idea
层序遍历，每层取最大值：result.append(max(level))。

## Complexity
- Time: O(n) — 每个节点访问一次
- Space: O(n) — 队列 + 结果

## Submission Log
- [x] Submitted on LeetCode (2026-11-02)
- [x] Passed all test cases
"""


# ============================================================
# LeetCode Submission (copy entire block to LeetCode)
# ============================================================
# 题目：每层节点中的最大值
# 思路：层序遍历，每层处理完后 result.append(max(level))
# 易错点：
#   - max(level) 取最大值
#   - 空树返回 []
from collections import deque
class Solution(object):
    def largestValues(self, root):
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
            level =[]
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(max(level))
        
        return result
