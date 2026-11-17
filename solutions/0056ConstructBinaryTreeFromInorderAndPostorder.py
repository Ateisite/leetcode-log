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

Idea:
  后序最后一个 = 根；在中序里找到根，左边左子树、右边右子树。
  后序切分：postorder[:idx] 给左，postorder[idx:-1] 给右（去掉末尾的根）。
  中序切分：inorder[:idx] / inorder[idx+1:]。

Complexity:
  Time: O(n²) — index() 线性查找 + 切片
  Space: O(n) — 递归栈 + 切片

Submission Log:
  2026-11-17: 首次提交，一次 AC（right_post 边界错一次后改对）
"""


class Solution(object):
    def buildTree(self, inorder, postorder):
        if not inorder:
            return None
        root_val = postorder[-1]
        root = TreeNode(root_val)
        idx = inorder.index(root_val)
        
        left_in = inorder[0:idx]
        right_in = inorder[idx+1:]

        left_post = postorder[0:idx]
        right_post = postorder[idx:-1]

        root.left = self.buildTree(left_in,left_post)
        root.right = self.buildTree(right_in,right_post)

        return root
