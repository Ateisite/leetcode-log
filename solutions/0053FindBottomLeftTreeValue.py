"""
#513 找树左下角的值 (Find Bottom Left Tree Value)
https://leetcode.cn/problems/find-bottom-left-tree-value/

题目要求：
  给定一棵二叉树，找到最后一层最左边的节点值。

示例：
  输入：
        2
       / \
      1   3
  输出：1

  输入：
        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7
  输出：7（最后一层是 [4,5,6]，但最左边是 4？不对，最后一层是 [7]，最左边是 7）

易错点：
  1. 不是找整棵树最左边的节点，是找最后一层最左边的
  2. 可以用 BFS 层序遍历，每层第一个就是最左边
  3. 也可以用 DFS 记录深度，找最深且最先访问的

思路：BFS 层序遍历，每层第一个节点就是最左边

Idea:
  层序遍历，每层第一个节点就是最左边。
  最后一层循环结束时，result 就是答案。

Complexity:
  Time: O(n) — 每个节点访问一次
  Space: O(w) — 队列最大宽度

Submission Log:
  2026-11-13: 首次提交，一次 AC
"""

from collections import deque
class Solution(object):
    def findBottomLeftValue(self, root):
        result = []
        if not root:
            return result
        queue = deque()
        queue.append(root)

        while queue:
            level = []
            size = len(queue)
            for _ in range(size):
              node = queue.popleft()
              level.append(node.val)
              if node.left:
                  queue.append(node.left)
              if node.right:
                  queue.append(node.right)
            result.append(level[0])
        return result[-1]
