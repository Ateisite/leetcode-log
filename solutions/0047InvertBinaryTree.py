"""
#226 翻转二叉树 (Invert Binary Tree)
https://leetcode.cn/problems/invert-binary-tree/

题目要求：
  给定一棵二叉树，翻转它（左右子树交换）。
  翻转后，每个节点的左右子树都互换位置。

示例：
  输入：
        4
       / \
      2   7
     / \ / \
    1  3 6  9
  输出：
        4
       / \
      7   2
     / \ / \
    9  6 3  1

易错点：
  1. 交换的是左右子树，不是节点的值
  2. 用 root.left, root.right = root.right, root.left 一行搞定
  3. 递归：先交换当前节点，再递归翻转子树（或者先递归再交换都行）

思路：DFS 递归，和 #104 最大深度一样的递归结构

Idea:
  递归翻转：先交换当前节点的左右子树，再递归翻转子树。

Complexity:
  Time: O(n) — 每个节点访问一次
  Space: O(h) — 递归栈深度，h 为树高

Submission Log:
  2026-11-07: 首次提交，一次 AC
"""


class Solution(object):
    def invertTree(self, root):
        def reverse(root):
            if not root:
                return root
            root.left, root.right = root.right, root.left
            reverse(root.left)
            reverse(root.right)
        reverse(root)
        return root

