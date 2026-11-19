"""
#617 合并二叉树 (Merge Two Binary Trees)
https://leetcode.cn/problems/merge-two-binary-trees/

题目要求：
  给定两棵二叉树 root1 和 root2，把它们合并成一棵新二叉树。
  规则：
  - 两个节点重叠 → 值相加，作为新节点的值
  - 只有一个存在 → 直接用那个节点
  - 都不存在 → None

示例：
  输入：root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
  输出：[3,4,5,5,4,null,7]

        1           2
       / \    +    / \
      3   2        1   3
     /     \      /     \
    5       7    4       7

        3
       / \
      4   5
     / \   \
    5   4   7

易错点：
  1. 两个都空 → 返回 None
  2. 只空一个 → 返回另一个（不用新建节点）
  3. 都不空 → 新建节点，值是两数之和
  4. 递归左右子树

思路：DFS 递归，同时遍历两棵树
"""


class Solution(object):
    def mergeTrees(self, root1, root2):
        # 在这里写代码
        pass
