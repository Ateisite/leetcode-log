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

Idea:
  中序遍历收集所有值 → Counter 统计次数 →
  找出最大次数 → 把所有次数等于最大次数的值收集返回。

Complexity:
  Time: O(n)
  Space: O(n)

Submission Log:
  2026-11-22: 首次提交，一次 AC
"""

from collections import Counter
class Solution(object):
    def findMode(self, root):
      if not root:
         return []
      result = []
      def inorder(node):
         if not node:
            return None
         inorder(node.left)
         result.append(node.val)
         inorder(node.right)
      inorder(root)
      cnt = Counter(result)
      max_count = max(cnt.values())
      res = []
      for k,v in cnt.items():
         if v == max_count:
            res.append(k)
      return res
      
