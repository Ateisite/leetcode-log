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

class Solution(object):
    def preorderTraversal(self, root):
        result  = []
        def dfs(node):
            if not node:
                return result
            result.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return result

class Solution(object):
    def postorderTraversal(self,root):
        result = []
        def dfs(node):
            if not node:
                return result
            dfs(node.left)
            dfs(node.right)
            result.append(node.val)
        dfs(root)
        return result


