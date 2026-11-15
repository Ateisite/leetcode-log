"""
#105 从前序与中序遍历序列构造二叉树 (Construct Binary Tree from Preorder and Inorder Traversal)
https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

题目要求：
  给定一棵树的前序遍历 preorder 和中序遍历 inorder，构造这棵二叉树并返回根节点。

示例：
  输入：preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
  输出：
        3
       / \
      9  20
        /  \
       15   7

易错点：
  1. 前序第一个元素 = 根节点
  2. 在中序里找到根，左边是左子树，右边是右子树
  3. 左右子树的大小决定前序里怎么切分
  4. 用哈希表存 inorder 的值→下标，避免每次线性查找

思路：递归。前序给根，中序分左右。
"""


class Solution(object):
    def buildTree(self, preorder, inorder):
        # 在这里写代码
        pass
