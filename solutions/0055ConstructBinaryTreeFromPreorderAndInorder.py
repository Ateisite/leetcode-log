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

Idea:
  前序第一个 = 根；在中序里找到根，左边是左子树、右边是右子树。
  idx（左子树节点数）决定前序怎么切：
      前序 [根][左 idx 个][右剩下]  → preorder[1:idx+1] / preorder[idx+1:]
      中序 [左 idx 个][根][右剩下]  → inorder[:idx] / inorder[idx+1:]
  递归构造左右子树。

Complexity:
  Time: O(n²) — index() 每次线性查找 + 切片复制；哈希表可优化到 O(n)
  Space: O(n) — 递归栈 + 切片

Submission Log:
  2026-11-16: 首次提交，一次 AC（Claude 代写讲解，用户理解后默写）
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def buildTree(self, preorder, inorder):
        # 1. 递归终止：数组空了，说明这棵子树不存在
        if not preorder:
            return None

        # 2. 前序的第一个就是根节点
        root_val = preorder[0]
        root = TreeNode(root_val)

        # 3. 在中序里找到根的位置
        #    idx = 左子树有几个节点
        idx = inorder.index(root_val)

        # 4. 切分数组
        #    前序：[根][左 idx 个][右剩下的]
        left_pre = preorder[1:idx+1]    # 跳过根，数 idx 个
        right_pre = preorder[idx+1:]    # 剩下的给右
        #    中序：[左 idx 个][根][右剩下的]
        left_in = inorder[:idx]         # 根左边
        right_in = inorder[idx+1:]      # 根右边

        # 5. 递归构造左右子树
        root.left = self.buildTree(left_pre, left_in)
        root.right = self.buildTree(right_pre, right_in)

        # 6. 返回根节点
        return root
