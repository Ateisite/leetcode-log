"""
#98 验证二叉搜索树 (Validate Binary Search Tree)
https://leetcode.cn/problems/validate-binary-search-tree/

题目要求：
  给定一棵二叉树，判断它是不是合法的二叉搜索树（BST）。
  BST 定义：左子树所有节点 < 根 < 右子树所有节点，且左右子树也都是 BST。

示例：
  输入：root = [5,1,4,null,null,3,6]
  输出：False（根是 5，但右子树里有 3 和 4，比 5 小）

        5
       / \
      1   4
         / \
        3   6

易错点：
  1. 只比较「当前节点和左右孩子」是不够的！
     比如上例：5 > 1 且 5 < 4 看着没问题，但 3 和 4 都在根的右边，应该 > 5
  2. 要传递「上下界」：每个节点必须在一个范围内
  3. 左孩子：上界变成当前节点值；右孩子：下界变成当前节点值

思路：DFS 递归，带上下界

Idea:
  check(node, low, high)：每个节点必须落在 (low, high) 内。
  左孩子上界收紧成 node.val，右孩子下界收紧成 node.val。
  初始边界用正负无穷。

Complexity:
  Time: O(n) — 每个节点访问一次
  Space: O(h) — 递归栈

Submission Log:
  2026-11-20: 首次提交，一次 AC（右子树写成left、初始边界写错，改后通过）
"""


class Solution(object):
    def isValidBST(self, root):
        if not root:
            return True
        def check(node,low,high):
            if not node:
                return True
            if not (low<node.val<high):
                return False
            return check(node.left,low,node.val) and check(node.right,node.val,high)
        return check(root,float('-inf'), float('inf'))
            
