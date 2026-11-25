"""
#701 二叉搜索树中的插入操作 (Insert into a Binary Search Tree)
https://leetcode.cn/problems/insert-into-a-binary-search-tree/

题目要求：
  给定一棵 BST 和一个值 val，把它插入到树中合适的位置，返回根节点。
  插入后仍然要是合法的 BST。

示例：
  输入：root = [4,2,7,1,3], val = 5
  输出：[4,2,7,1,3,5]

        4
       / \
      2   7
     / \ /
    1  3 5

易错点：
  1. 走到空节点 → 说明找到位置了，新建节点返回
  2. val < root.val → 往左；val > root.val → 往右
  3. 递归返回的新子树要接回 root.left / root.right
  4. 最后返回 root

思路：递归往下找空位，找到就插入

Idea:
  空节点 = 插入位置 → 新建节点返回；
  否则按大小往左/右走，递归结果接回 root.left / root.right。

Complexity:
  Time: O(h)
  Space: O(h)

Submission Log:
  2026-11-25: 首次提交，一次 AC
"""


class Solution(object):
    def insertIntoBST(self, root, val):
        if not root:
            return TreeNode(val)
        if root.val > val:
            root.left = self.insertIntoBST(root.left,val)
        if root.val < val:
            root.right = self.insertIntoBST(root.right,val)
        return root
