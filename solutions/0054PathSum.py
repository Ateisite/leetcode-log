"""
#112 路径总和 (Path Sum)
https://leetcode.cn/problems/path-sum/

题目要求：
  给定一棵二叉树和一个目标值 targetSum，
  判断是否存在从根节点到叶子节点的路径，使得路径上所有节点值之和等于 targetSum。

示例：
  输入：
        5
       / \
      4   8
     /   / \
    11  13  4
   /  \      \
  7    2      1
  targetSum = 22
  输出：True（5+4+11+2 = 22）

易错点：
  1. 必须是到「叶子节点」的路径，中途节点不算
  2. 思路：每走一步就减去当前节点值，到叶子时判断是否为 0
  3. 空树返回 False

思路：DFS 递归，累加路径和，叶子节点判断

Idea:
  dfs(node, path) 累加路径和，叶子节点判断 sum(path) == targetSum。
  回溯：append 和 pop 必须成对，叶子节点 return 前也要 pop。

Complexity:
  Time: O(n²) — 每个叶子求一次 sum
  Space: O(h) — 递归栈深度

Submission Log:
  2026-11-14: 首次提交，一次 AC（叶子漏 pop 调试后通过）
"""


class Solution(object):
    def hasPathSum(self, root, targetSum):
        if not root:
            return False

        def dfs(node, path):
            if not node:
                return False

            path.append(node.val)

            if not node.left and not node.right:
                res = sum(path) == targetSum
                path.pop()
                return res

            left = dfs(node.left, path)
            right = dfs(node.right, path)
            path.pop()
            return left or right

        return dfs(root, [])

        
