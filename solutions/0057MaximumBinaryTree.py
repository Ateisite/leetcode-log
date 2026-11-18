"""
#654 最大二叉树 (Maximum Binary Tree)
https://leetcode.cn/problems/maximum-binary-tree/

题目要求：
  给定一个不重复的整数数组 nums，构造一棵「最大二叉树」：
  - 根节点是数组中的最大值
  - 左子树是最大值左边部分构造出的最大二叉树
  - 右子树是最大值右边部分构造出的最大二叉树

示例：
  输入：nums = [3,2,1,6,0,5]
  输出：
          6
        /   \
       3     5
        \    /
         2  0
          \
           1

易错点：
  1. 找最大值：max(nums)，再找它的下标 nums.index(max_val)
  2. 切成左右两段，递归
  3. 空数组返回 None

思路：和 #105/#106 一个套路 —— 找根，切两刀，递归

Idea:
  数组里的最大值当根，下标 idx 左边给左子树、右边给右子树，递归。
  嵌套函数 findmax 直接调用（不用 self）。

Complexity:
  Time: O(n²) — 每层 max() + index() 都是 O(n)
  Space: O(n) — 递归栈

Submission Log:
  2026-11-18: 首次提交，一次 AC
"""


class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        if not nums:
            return None
        def findmax(nums):
            if not nums:
              return None
            root_val = max(nums)
            root = TreeNode(root_val)
            idx = nums.index(root_val)
            left = nums[:idx]
            right = nums[idx+1:]
            root.left = findmax(left)
            root.right = findmax(right)
            return root
            
        return findmax(nums)