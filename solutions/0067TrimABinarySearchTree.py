"""
#669 修剪二叉搜索树 (Trim a Binary Search Tree)
https://leetcode.cn/problems/trim-a-binary-search-tree/

题目要求：
  给定一棵 BST 的根节点 root 和一个范围 [low, high]，
  修剪这棵树，使所有节点的值都在 [low, high] 内。修剪后仍是 BST。

示例：
  输入：root = [1,0,2], low = 1, high = 2
  输出：[1,null,2]

        1
       / \
      0   2

  0 < 1 → 左子树整个剪掉
  修剪后：
        1
         \
          2

易错点：
  1. root.val < low → 左子树所有节点都 < low → 整棵左子树都不要，答案在右子树
  2. root.val > high → 右子树所有节点都 > high → 整棵右子树都不要，答案在左子树
  3. 在范围内 → 保留 root，递归修剪左右
  4. 递归结果接回 root.left / root.right

思路：递归，利用 BST 性质整棵子树地剪
"""


class Solution(object):
    def trimBST(self, root, low, high):
        # 在这里写代码
        pass
