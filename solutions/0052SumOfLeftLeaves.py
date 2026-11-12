"""
#404 左叶子之和 (Sum of Left Leaves)
https://leetcode.cn/problems/sum-of-left-leaves/

题目要求：
  给定一棵二叉树，返回所有左叶子节点的值之和。
  左叶子 = 是父节点的左孩子，且没有子节点。

示例：
  输入：
        3
       / \
      9  20
        /  \
       15   7
  输出：24（9 + 15 = 24）

易错点：
  1. 左叶子 ≠ 左子节点，必须是叶子（没有子节点）
  2. 要判断「是左孩子」：可以通过参数传递
  3. 右子树中的左叶子也要算

思路：DFS 递归，判断当前节点是否为左叶子

Idea:
  dfs(node, is_left)：is_left 标记当前节点是否是父节点的左孩子。
  如果是左孩子且是叶子 → 返回节点值；否则递归左右子树。

Complexity:
  Time: O(n) — 每个节点访问一次
  Space: O(h) — 递归栈深度

Submission Log:
  2026-11-12: 首次提交，一次 AC
"""


class Solution(object):
    def sumOfLeftLeaves(self, root):
        result = 0
        def dfs(node,is_left):
            if not node:
                return 0

            if is_left and not node.left and not node.right:
                return node.val
            
            return dfs(node.left,True) + dfs(node.right,False)
        result += dfs(root,False)
        return result
