"""
#111 二叉树的最小深度 (Minimum Depth of Binary Tree)
https://leetcode.cn/problems/minimum-depth-of-binary-tree/

题目要求：
  给定一个二叉树，找出其最小深度。
  最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
  叶子节点是指没有子节点的节点。

易错点：
  1. 一边子树为空时，不能算 0，要走另一边！
     比如只有右子树的树，最小深度不是 0+1=1，而是右子树的深度+1
  2. 只有左右子树都存在时，才取 min(左, 右)
  3. 叶子节点判断：if not root.left and not root.right: return 1
  4. 空树深度为 0：if not root: return 0

思路：DFS 递归，和 #104 最大深度类似，但处理一边为空的情况

Idea:
  递归算左右子树深度，如果一边为 0（空），只能走另一边；
  两边都有才取 min。

Complexity:
  Time: O(n) — 每个节点访问一次
  Space: O(h) — 递归栈深度，h 为树高

Submission Log:
  2026-11-06: 首次提交，一次 AC
"""


class Solution(object):
    def minDepth(self, root):
        if not root:
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if left == 0:
            return right +1
        if right == 0:
            return left + 1
        return min(left,right)+1

        
