"""
#106 从中序与后序遍历序列构造二叉树 (Construct Binary Tree from Inorder and Postorder Traversal)
https://leetcode.cn/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

题目要求：
  给定一棵树的中序遍历 inorder 和后序遍历 postorder，构造这棵二叉树并返回根节点。

示例：
  输入：inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
  输出：
        3
       / \
      9  20
        /  \
       15   7

易错点：
  1. 后序是「左→右→根」，所以最后一个元素才是根
  2. 在中序里找到根，左边是左子树，右边是右子树
  3. 后序切分：postorder[:idx] 给左，postorder[idx:-1] 给右（去掉最后的根）
  4. 空数组返回 None

思路：和 #105 几乎一样，只是根从「前序第一个」变成「后序最后一个」
"""


class Solution(object):
    def buildTree(self, inorder, postorder):
        # 在这里写代码
        pass
