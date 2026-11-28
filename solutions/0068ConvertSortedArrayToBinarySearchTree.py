"""
#108 将有序数组转换为二叉搜索树 (Convert Sorted Array to Binary Search Tree)
https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/

题目要求：
  给定一个升序数组 nums，把它转换成一棵「高度平衡」的二叉搜索树。
  高度平衡：每个节点的左右子树高度差不超过 1。

示例：
  输入：nums = [-10,-3,0,5,9]
  输出：[0,-3,9,-10,null,5]

        0
       / \
     -3   9
     /   /
   -10  5

易错点：
  1. 取中间元素当根：mid = len(nums) // 2
  2. 中间元素的左边全在左子树，右边全在右子树（因为是升序）
  3. 递归左右，结果接回 root.left / root.right
  4. 空数组返回 None

思路：中间元素当根，递归左右
"""


class Solution(object):
    def sortedArrayToBST(self, nums):
        # 在这里写代码
        pass
