"""
#222 完全二叉树的节点个数 (Count Complete Tree Nodes)
https://leetcode.cn/problems/count-complete-tree-nodes/

题目要求：
  给定一棵完全二叉树，返回节点个数。
  完全二叉树：每一层都填满，最后一层从左到右连续填充。

示例：
  输入：
        1
       / \
      2   3
     / \  /
    4  5 6
  输出：6

易错点：
  1. 完全二叉树 ≠ 满二叉树，最后一层可能没满
  2. 利用完全二叉树特性：如果最左深度 == 最右深度，则是满二叉树，节点数 = 2^h - 1
  3. 否则递归：1 + 左子树节点数 + 右子树节点数
  4. 求最左深度：一直往左走；求最右深度：一直往右走

思路：DFS 递归，利用完全二叉树特性优化，比暴力遍历快

Idea:
  求最左深度和最右深度，如果相等则是满二叉树，直接返回 2^h - 1。
  否则递归：1 + 左子树 + 右子树。

Complexity:
  Time: O(log²n) — 利用完全二叉树特性，避免遍历每个节点
  Space: O(log n) — 递归栈深度

Submission Log:
  2026-11-09: 首次提交，一次 AC
"""


class Solution(object):
    def countNodes(self, root):
        if not root:
            return 0

        # 求最左深度
        left_depth = 0
        node = root
        while node:
            left_depth += 1
            node = node.left

        # 求最右深度
        right_depth = 0
        node = root
        while node:
            right_depth += 1
            node = node.right

        # 如果相等 → 满二叉树
        if left_depth == right_depth:
            return 2 ** left_depth - 1

        # 否则递归
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)


    
            
