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

Idea:
  找到 key 后分 5 种情况：没找到/叶子/只有右/只有左/两个都有。
  两个都有：用右子树最小值覆盖当前节点，再递归删掉那个最小值。
  递归结果必须接回 root.left/right，最后 return root。

Complexity:
  Time: O(h)
  Space: O(h)

Submission Log:
  2026-11-26: 首次提交，一次 AC
"""


class Solution(object):
    def deleteNode(self, root, key):
        if not root:
            return None
        if root.val == key:
            if not root.left and not root.right:
                return None
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            min_node = root.right
            while min_node.left:
                min_node = min_node.left
            root.val = min_node.val
            root.right = self.deleteNode(root.right,min_node.val)
            return root
        if root.val < key:
            root.right = self.deleteNode(root.right,key)
        if root.val > key:
            root.left = self.deleteNode(root.left,key)
        return root