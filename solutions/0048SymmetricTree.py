"""
#101 对称二叉树 (Symmetric Tree)
https://leetcode.cn/problems/symmetric-tree/

题目要求：
  给定一棵二叉树，判断它是否镜像对称（轴对称）。
  即：左子树和右子树镜像对称。

示例：
  输入：
        1
       / \
      2   2
     / \ / \
    3  4 4  3
  输出：True

  输入：
        1
       / \
      2   2
       \   \
        3   3
  输出：False

易错点：
  1. 不是比较单个节点，是比较两个子树是否镜像
  2. 左子树的左 == 右子树的右，左子树的右 == 右子树的左
  3. 需要辅助函数 compare(left, right) 递归比较两个节点
  4. 空树是对称的

思路：DFS 递归，类似 #226 翻转，但比较的是两个子树而不是一个

Idea:
  辅助函数 compare(left, right) 递归比较两个子树是否镜像。
  两个都空→True，一个空→False，值不等→False。
  递归：左的左 vs 右的右，左的右 vs 右的左。

Complexity:
  Time: O(n) — 每个节点访问一次
  Space: O(h) — 递归栈深度

Submission Log:
  2026-11-08: 首次提交，一次 AC
"""


class Solution(object):
    def isSymmetric(self, root):
        # 在这里写代码
        
        def compare(left,right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            return compare(left.left, right.right) and compare(left.right, right.left)
        return compare(root.left,root.right)