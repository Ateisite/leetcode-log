"""
#235 二叉搜索树的最近公共祖先 (Lowest Common Ancestor of a Binary Search Tree)
https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-search-tree/

题目要求：
  给定一棵**二叉搜索树**（BST）和两个节点 p、q，找它们的最近公共祖先。

示例：
  输入：root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
  输出：6

          6
        /   \
       2     8
      / \   / \
     0   4 7   9
        / \
       3   5

易错点：
  1. 这是 BST！可以用大小关系，不用像 #236 那样遍历整棵树
  2. p、q 都小于 root → LCA 在左子树
  3. p、q 都大于 root → LCA 在右子树
  4. 否则（分居两侧，或其中一个就是 root）→ root 就是 LCA

思路：利用 BST 左小右大，每次淘汰一半

Idea:
  p、q 都小于 root → LCA 在左子树；
  p、q 都大于 root → LCA 在右子树；
  否则（分居两侧，或其中一个就是 root）→ root 就是 LCA。
  只走一边，比 #236 快。

Complexity:
  Time: O(h) — 只走一条路径
  Space: O(h) — 递归栈

Submission Log:
  2026-11-24: 首次提交，一次 AC
"""


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if not root or root.val == p or root.val == q:
            return root
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right,p,q)
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left,p,q)
        return root
