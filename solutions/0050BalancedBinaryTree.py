"""
#110 平衡二叉树 (Balanced Binary Tree)
https://leetcode.cn/problems/balanced-binary-tree/

题目要求：
  给定一棵二叉树，判断它是否是平衡二叉树。
  平衡二叉树：每个节点的左右子树高度差不超过 1。

示例：
  输入：
        3
       / \
      9  20
        /  \
       15   7
  输出：True（每个节点左右高度差 ≤ 1）

  输入：
        1
       / \
      2   2
     / \
    3   3
   / \
  4   4
  输出：False（根节点左子树高度3，右子树高度1，差=2）

易错点：
  1. 不是只判断根节点，每个节点都要判断
  2. 需要同时知道「高度」和「是否平衡」
  3. 可以用 -1 表示不平衡，省去重复计算
  4. 空树是平衡的

思路：DFS 递归，和 #104 最大深度类似，但多返回一个是否平衡的信息

Idea:
  辅助函数 check(root) 返回高度，不平衡返回 -1。
  主函数判断 check(root) != -1。

Complexity:
  Time: O(n) — 每个节点访问一次
  Space: O(h) — 递归栈深度

Submission Log:
  2026-11-10: 首次提交，一次 AC
"""


class Solution(object):
    def isBalanced(self, root):
        def check(root):
          if not root:
              return 0
          left = check(root.left)
          right = check(root.right)

          if left == -1 or right == -1:  # 有一边不平衡
            return -1

          if abs(left - right) > 1:      # 高度差>1
            return -1

          return max(left, right) + 1    # 返回高度 
        result = check(root)
        return True if result !=-1 else False