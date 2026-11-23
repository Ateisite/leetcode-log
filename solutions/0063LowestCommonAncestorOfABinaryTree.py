"""
#236 二叉树的最近公共祖先 (Lowest Common Ancestor of a Binary Tree)
https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/

题目要求：
  给定一棵二叉树和两个节点 p、q，找到它们的「最近公共祖先」（LCA）。
  LCA = 最深的那个节点，它同时是 p 和 q 的祖先。

示例：
  输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
  输出：3

          3
        /   \
       5     1
      / \   / \
     6   2 0   8
        / \
       7   4

  5 和 1 的公共祖先是 3

易错点：
  1. 当前节点自己可能就是 p 或 q
  2. p 和 q 可能一个在左子树一个在右子树 → 当前节点就是 LCA
  3. 也可能一个节点是另一个的祖先
  4. 用「左右各找到什么」来判断

思路：DFS 递归，看左右子树各能找到什么
"""


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        # 在这里写代码
        pass
