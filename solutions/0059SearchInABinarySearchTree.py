"""
#700 二叉搜索树中的搜索 (Search in a Binary Search Tree)
https://leetcode.cn/problems/search-in-a-binary-search-tree/

题目要求：
  给定一棵二叉搜索树（BST）和一个目标值 val，
  找到值为 val 的节点，返回以它为根的子树；如果不存在，返回 None。

示例：
  输入：root = [4,2,7,1,3], val = 2
  输出：[2,1,3]

        4
       / \
      2   7
     / \
    1   3

易错点：
  1. BST 性质：左子树所有节点 < 根 < 右子树所有节点
  2. 利用这个性质可以「只走一边」，不用遍历整棵树
  3. val == root.val → 找到，返回 root
  4. val < root.val → 只往左找；val > root.val → 只往右找
  5. 走到空还没找到 → 返回 None

思路：递归，每次只走一边（这就是 BST 搜索快的原因）

Idea:
  BST 左小右大：val < root.val 往左，val > root.val 往右，
  相等就返回该节点，走到空返回 None。

Complexity:
  Time: O(h) — h 为树高，BST 平均 O(log n)，最坏 O(n)
  Space: O(h) — 递归栈

Submission Log:
  2026-11-19: 首次提交，一次 AC（补 11-15 的课）
"""


class Solution(object):
    def searchBST(self, root, val):
        if not root:
            return None
        if root.val == val:
            return root
        if root.val > val:
            return self.searchBST(root.left,val)
        if root.val < val:
            return self.searchBST(root.right,val)
        
