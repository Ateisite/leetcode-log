 """
复习默写 — 白纸写，不看笔记
写完让 Claude 对照

每道题的注释包括：
  1. 题目要求（一句话）
  2. 易错点 / 你之前踩过的坑
复习时看注释回忆，不要看下面的代码。
"""

# === 第1题：反转链表（#206） ===
# 题目：反转单链表，返回新头节点
# 易错点：
#   - 必须先保存 next 再改指针，否则断链
#   - 用 dummy 节点做头插法，最后返回 dummy.next

class ListNode(object):
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self,head):
        result = ListNode()
        while head:
            nextnode = head.next
            head.next = result.next
            result.next = head
            head = nextnode
        return result.next

# === 第2题：罗马数字转整数（#13） ===
# 题目：罗马数字字符串 → 整数
# 易错点：
#   - 初始 result 取 s[0] 的值，不是 0
#   - 比较 s[i] 和 s[i+1]，不是 s[i-1]
#   - 最后一位 s[-1] 直接加上，不参与比较
#   - 当前值 < 右边 → 减；否则 加

class Solution(object):
    def romanToInt(self,s):
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = 0
        for i in range(len(s)-1):
            if roman[s[i]]>=roman[s[i+1]]:
                result += roman[s[i]]
            else:
                result -= roman[s[i]]
        result = result + roman[s[len(s)-1]]
        return result

# === 第3题：快速幂（#50） ===
# 题目：计算 x^n，n 可能为负数
# 易错点：
#   - 用 abs(n) 做循环，最后再取倒数（不要一开始就 1/x）
#   - m%2==1 时乘到 result，然后 x=x*x, m=m//2
#   - n==0 时返回 1（while 循环不执行，result 初始就是 1）

class Solution(object):
    def myPow(self, x, n):
        result = 1
        m = abs(n)
        while m>0:
            if m%2 == 1:
                result *= x
            x *= x
            m = m // 2
        return result if n > 0 else 1/result

# === 第4题：两数相加（#2） ===
# 题目：两个逆序链表表示的数相加，返回和的链表
# 易错点：
#   - total = v1 + v2 + carry（用 carry，不是上一轮的 total！）
#   - current.next = ListNode(...)，不是 current = ListNode(...)
#   - 提交时删掉自定义 ListNode 类，LeetCode 自带
#   - 长度不等用 val if node else 0

class Solution(object):
    def addTwoNumbers(self,l1,l2):
        dummy = ListNode()
        current = dummy
        carry = 0
        total = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            total = v1 + v2 + carry
            carry = total //10
            current.next = ListNode(total%10)
            current = current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next

# === 第5题：合并有序链表（#21） ===
# 题目：合并两个升序链表为一个升序链表
# 易错点：
#   - while 条件用 and（两个都不空才比较）
#   - 循环结束后拼接剩余：current.next = list1 if list1 else list2
#   - 链表不能用索引，用 node.val 和 node.next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        current = dummy
        while list1 and list2:
            if list1.val<=list2.val:
                current.next = list1
                list1 = list1.next
                current = current.next
            else:
                current.next = list2
                list2 = list2.next
                current = current.next
        current.next = list1 if list1 else list2
        return dummy.next

# === 第6题：两数相加II（#445） ===
# 题目：两个正序链表（高位在前）表示的数相加
# 易错点：
#   - 思路：反转 → 相加（同#2）→ 再反转
#   - addTwoNumbers1 中：current.next = ListNode(...)，不是 current = ListNode(...)
#   - 提交时删掉自定义 ListNode 类

class Solution(object):
    def reverseList(self, head):
        dummy = ListNode()
        while head:
            next_node = head.next
            head.next = dummy.next
            dummy.next = head
            head = next_node
        return dummy.next
    def addTwoNumbers1(self, l1, l2):
        dummy = ListNode()
        current = dummy
        carry = 0
        total = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            total =v1+v2+carry
            current.next = ListNode(total%10)
            carry = total//10
            current = current.next
            if l1:l1 = l1.next
            if l2: l2 = l2.next
        return dummy.next
    def addTwoNumbers(self, l1, l2):
        result = 0
        l1 = self.reverseList(l1)
        l2 = self.reverseList(l2)
        result = self.reverseList(self.addTwoNumbers1(l1,l2))
        return result

# === 第7题：二叉树前序遍历（#144） ===
# 题目：根→左→右，返回节点值列表
# 易错点：
#   - 嵌套函数共享外层 result 列表
#   - append 在递归左、右之间（最前面）
#   - 基准：if not node: return

class Solution(object):
    def preorderTraversal(self, root):
        result  = []
        def dfs(node):
            if not node:
                return
            result.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return result

# === 第8题：二叉树后序遍历（#145） ===
# 题目：左→右→根，返回节点值列表
# 易错点：
#   - append 在最后（递归左、右之后）
#   - 嵌套函数不要加 self

class Solution(object):
    def postorderTraversal(self,root):
        result = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            result.append(node.val)
        dfs(root)
        return result

# === 第9题：快速幂（#50） ===
# 题目：计算 x^n，n 可能为负数
# 易错点：
#   - 用 abs(n) 做循环，最后再取倒数
#   - m%2==1 时乘到 result

class Solution(object):
    def myPow(self,x,n):
        result = 1
        m = abs(n)
        while m > 0:
            if m % 2 ==1:
                result *= x
            x *= x
            m = m // 2
        return result if n > 0 else 1/result

# === 第10题：两数相加（#2） ===
# 题目：两个逆序链表相加，返回和的链表
# 易错点：
#   - total = v1 + v2 + carry（用 carry，不是上一轮的 total）
#   - current.next = ListNode(...)，不是 current = ListNode(...)

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        current = dummy
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            total = v1 + v2 + carry
            current.next = ListNode(total%10)
            carry = total // 10
            current = current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next

# === 第11题：二叉树层序遍历（#102） ===
# 题目：从上到下、从左到右，按层返回节点值（二维列表）
# 易错点：
#   - from collections import deque
#   - deque([root]) 要加中括号
#   - size = len(queue) 在 for 外记录
#   - popleft() 不是 pop()
#   - 空树返回 []
from collections import deque
class Solution(object):
    def levelOrder(self, root):
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
            result.append(level)
        return result
        

# === 第12题：二叉树右视图（#199） ===
# 题目：站在二叉树右边看，能看到的节点值（从上到下）
# 易错点：
#   - 层序遍历每层取 level[-1]
#   - 空树返回 []


from collections import deque
class Solution(object):
    def levelOrder(self, root):
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
            result.append(level[-1])
        return result

# === 第13题：二叉树层序遍历II（#107） ===
# 题目：层序遍历，结果从下到上
# 易错点：
#   - 方法名是 levelOrderBottom
#   - result.reverse() 返回 None，要先调用再 return
from collections import deque
class Solution(object):
    def levelOrderBottom(self, root):
        result = []
        if not root:
            return result
        queue = deque()
        queue.append(root)

        while queue:
            level =[]
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        result.reverse()
        return result

# === 第14题：二叉树层平均值（#637） ===
# 题目：每层节点的平均值
# 易错点：
#   - popleft() 别忘括号
#   - 除以 len(level) 不是 len(queue)
#   - Python 2 整数除法问题（选 Python 3 提交）
from collections import deque
class Solution(object):
    def averageOfLevels(self, root):
        result = []
        if not root:
            return result
        queue = deque()
        queue.append(root)

        while queue:
            level =[]
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            average = sum(level)/len(level)
            result.append(average)
        return result

# === 第15题：N叉树层序遍历（#429） ===
# 题目：N叉树按层返回节点值
# 易错点：
#   - 用 for child in node.children，不是 left/right
#   - 空树返回 []
from collections import deque
class Solution(object):
    def levelOrder(self, root):
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
                for child in node.children:
                    queue.append(child)
            result.append(level)
        return result

# === 第16题：每行最大值（#515） ===
# 题目：每层节点中的最大值
# 易错点：
#   - max(level) 取最大值
#   - 空树返回 []
from collections import deque
class Solution(object):
    def largestValues(self, root):
        result = []
        if not root:
            return result
        queue = deque()
        queue.append(root)

        while queue:
            level =[]
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(max(level))
        return result

# === 第17题：填充next指针（#116） ===
# 题目：完美二叉树，每个节点的 next 指向同层右边的节点
# 易错点：
#   - level 存节点，不是值（level.append(node)）
#   - 
#   - 返回 root，不是 result
from collections import deque
class Solution(object):
    def connect(self, root):
        
        if not root:
            return root
        queue = deque()
        queue.append(root)

        while queue:
            level = []
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                level.append(node)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            for i in range(len(level)-1):
                level[i].next = level[i+1]
        return root

# === 第18题：二叉树层序遍历（#102） ===
# 题目：从上到下、从左到右，按层返回节点值（二维列表）
# 易错点：
#   - deque([root]) 要加中括号
#   - size = len(queue) 在 for 外记录
#   - popleft() 不是 pop()
#   - 空树返回 []
from collections import deque
class Solution(object):
    def levelOrder(self, root):
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
            result.append(level)
        return result

# === 第19题：填充next指针II（#117） ===
# 题目：普通二叉树，每个节点的 next 指向同层右边的节点
# 易错点：
#   - 同 #116，level 存节点不是值
#   - 返回 root
from collections import deque
class Solution(object):
    def connect(self, root):
        
        if not root:
            return root
        queue = deque()
        queue.append(root)

        while queue:
            level = []
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                level.append(node)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            for i in range(len(level)-1):
                level[i].next = level[i+1]
        return root


# === 第20题：二叉树右视图（#199） ===
# 题目：站在二叉树右边看，能看到的节点值（从上到下）
# 易错点：
#   - 层序遍历每层取 level[-1]
#   - 空树返回 []
from collections import deque
class Solution(object):
    def rightSideView(self, root):
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
            result.append(level[-1])
        return result

# === 第21题：二叉树最大深度（#104） ===
# 题目：二叉树的最大深度（根到最远叶子）
# 易错点：
#   - 递归：max(左, 右) + 1
#   - 基准：if not root: return 0

class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        return max(self.maxDepth(root.left),self.maxDepth(root.right))+1

# === 第22题：填充next指针II（#117） ===
# 题目：普通二叉树，每个节点的 next 指向同层右边的节点
# 易错点：
#   - 同 #116，level 存节点不是值
#   - 返回 root
from collections import deque
class Solution(object):
    def connect(self, root):
        if not root:
            return root
        queue = deque()
        queue.append(root)
        while queue:
            level = []
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                level.append(node)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            for i in range(len(level)-1):
                level[i].next = level[i+1]
        return root

# === 第23题：二叉树的最小深度（#111） ===
# 题目：给定二叉树，返回最小深度（根到最近叶子节点的节点数）
# 易错点：
#   - 一边子树为空时，不能算 0，要走另一边
#   - 只有左右都有时，才取 min(左, 右)
#   - 叶子节点：if not root.left and not root.right: return 1

class Solution(object):
    def minDepth(self, root):
        # 在这里默写
        pass