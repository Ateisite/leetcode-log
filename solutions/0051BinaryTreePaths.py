"""
#257 二叉树的所有路径 (Binary Tree Paths)
https://leetcode.cn/problems/binary-tree-paths/

题目要求：
  给定一棵二叉树，返回所有从根节点到叶子节点的路径。
  每条路径用字符串表示，节点之间用 "->" 连接。

示例：
  输入：
        1
       / \
      2   3
       \
        5
  输出：["1->2->5", "1->3"]

易错点：
  1. 叶子节点 = 没有子节点的节点
  2. 路径是根到叶子，不是任意节点
  3. 字符串拼接：path + "->" + str(node.val)
  4. 回溯：每次递归要复制路径，不要共享同一个列表

思路：DFS 递归 + 路径记录（回溯）
"""


class Solution(object):
    def binaryTreePaths(self, root):
        # 在这里写代码
        pass
