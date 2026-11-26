"""
#450 删除二叉搜索树中的节点 (Delete Node in a BST)
https://leetcode.cn/problems/delete-node-in-a-bst/

题目要求：
  给定一棵 BST 的根节点 root 和一个值 key，删除值为 key 的节点，
  返回删除后的根节点。删除后仍要是合法 BST。

示例：
  输入：root = [5,3,6,2,4,null,7], key = 3
  输出：[5,4,6,2,null,null,7]

        5
       / \
      3   6
     / \   \
    2   4   7

  删除 3 后，用左子树最大值 2 或右子树最小值 4 顶上：
        5
       / \
      4   6
     /     \
    2       7

易错点：
  1. 分 5 种情况：没找到 / 叶子 / 只有右 / 只有左 / 两个都有
  2. 两个都有时：用「右子树的最小值」（一直往左走到底）替换当前节点，
     然后递归删掉那个最小值
  3. 删除结果要接回 root.left / root.right

思路：先找到 key，再分情况处理
"""


class Solution(object):
    def deleteNode(self, root, key):
        # 在这里写代码
        pass
