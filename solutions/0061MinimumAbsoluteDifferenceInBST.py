"""
#530 二叉搜索树的最小绝对差 (Minimum Absolute Difference in BST)
https://leetcode.cn/problems/minimum-absolute-difference-in-bst/

题目要求：
  给定一棵二叉搜索树（BST），返回**任意两个节点值之差的最小绝对值**。

示例：
  输入：root = [4,2,6,1,3]
  输出：1

        4
       / \
      2   6
     / \
    1   3

易错点：
  1. 不是只比较父子和左右孩子，要比较所有节点对
  2. 关键性质：BST 的「中序遍历」是**递增**的
     → 最小差一定出现在**中序相邻**的两个节点之间
  3. 中序遍历：左 → 根 → 右

思路：中序遍历收集所有值，再比较相邻差

Idea:
  BST 中序遍历是递增的 → 最小差一定在相邻两个节点之间。
  中序遍历存列表，再遍历一遍比较相邻差。

Complexity:
  Time: O(n)
  Space: O(n)

Submission Log:
  2026-11-21: 首次提交，一次 AC
"""


class Solution(object):
    def getMinimumDifference(self, root):
        if not root:
            return 0
        res = []
        def dfs(node):
            
            if not node:
                return 
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
            
        dfs(root)
        diff = float('inf')
        for i in range(len(res)-1):
            diff = min(diff,res[i+1]-res[i])
        return diff
