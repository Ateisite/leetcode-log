"""
#501 二叉搜索树中的众数 (Find Mode in Binary Search Tree)
https://leetcode.cn/problems/find-mode-in-binary-search-tree/

题目要求：
  给定一棵**有重复值**的二叉搜索树，找出所有「众数」（出现次数最多的值）。
  众数可能不止一个，全部返回。

示例：
  输入：root = [1,null,2,2]
  输出：[2]

  输入：root = [0]
  输出：[0]

易错点：
  1. 众数可能有多个，要全部收集
  2. 还是利用 BST 性质：中序遍历递增 → 相同的值会**连续出现**
  3. 统计连续相同值的个数，就是该值的出现次数
  4. 空树返回 []

思路：中序遍历 + 计数（相同的值挨在一起，数起来很方便）
"""


class Solution(object):
    def findMode(self, root):
        # 在这里写代码
        pass
