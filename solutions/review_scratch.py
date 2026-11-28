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
# 题目：给定二叉树，返回每层节点值的平均值（列表）
# 示例：[3,9,20,null,null,15,7] → [3, 14.5, 11]
# 易错点：
#   - popleft() 别忘括号
#   - 除以 len(level) 不是 len(queue)
#   - average 放在 for 循环外面，和 result.append 同级
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
# 示例：[3,9,20,null,null,15,7] → 2；[1,null,2] → 2（不能算左边空的0）
# 易错点：
#   - 一边子树为空时，不能算 0，要走另一边！
#   - 先算左右，再判断谁是 0；两边都有才取 min
#   - 只有 not root.left and not root.right 才是叶子

class Solution(object):
    def minDepth(self, root):
        if not root:
            return 0

        left =  self.minDepth(root.left)
        right = self.minDepth(root.right)
        if left == 0:
            return right+1
        if right == 0:
            return left +1
        return min(left,right)+1

# === 第24题：二叉树层平均值（#637） ===
# 题目：给定二叉树，返回每层节点值的平均值（列表）
# 示例：[3,9,20,null,null,15,7] → [3, 14.5, 11]
# 易错点：
#   - popleft() 别忘括号
#   - 除以 len(level) 不是 len(queue)
#   - average 放在 for 循环外面，和 result.append 同级
#   - Python 2 整数除法问题（选 Python 3 提交）
from collections import deque
class Solution(object):
    def averageOfLevels(self, root):
        result = []
        if not root:
            return result
        queue=deque()
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
            average = sum(level)/len(level)
            result.append(average)
        return result

# === 第25题：翻转二叉树（#226） ===
# 题目：给定二叉树，翻转它（每个节点的左右子树互换）
# 示例：[4,2,7,1,3,6,9] → [4,7,2,9,6,3,1]
# 易错点：
#   - 交换的是左右子树，不是节点的值
#   - root.left, root.right = root.right, root.left 一行搞定
#   - 递归：先交换再递归，或先递归再交换都行
#   - 空树返回 None

class Solution(object):
    def invertTree(self, root):
        def reverse(root):
            if not root:
                return root
            root.left,root.right = root.right,root.left
            reverse(root.left)
            reverse(root.right)
        reverse(root)
        return root

# === 第26题：二叉树最大深度（#104） ===
# 题目：给定二叉树，返回最大深度（根到最远叶子节点的节点数）
# 示例：[3,9,20,null,null,15,7] → 3
# 易错点：
#   - 基准：if not root: return 0
#   - 递归：return max(左, 右) + 1
#   - 返回的是 root，不是 result
class Solution(object):
    def maxDepth(self, root):
        # 在这里默写
        if not root:
            return 0
        return max(self.maxDepth(root.left),self.maxDepth(root.right))+1

# === 第27题：对称二叉树（#101） ===
# 题目：判断二叉树是否镜像对称
# 示例：[1,2,2,3,4,4,3] → True；[1,2,2,null,3,null,3] → False
# 易错点：
#   - 辅助函数 compare(left, right) 比较两个子树
#   - 左的左 vs 右的右，左的右 vs 右的左
#   - 两个都空→True，一个空→False，值不等→False
class Solution(object):
    def isSymmetric(self, root):
        def compare(left,right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            return compare(left.left,right.right) and compare(left.right,right.left)
        return compare(root.left,root.right)

# === 第28题：二叉树最小深度（#111） ===
# 题目：给定二叉树，返回最小深度（根到最近叶子节点的节点数）
# 示例：[3,9,20,null,null,15,7] → 2；[1,null,2] → 2（不能算左边空的0）
# 易错点：
#   - 一边子树为空时，不能算 0，要走另一边！
#   - 先算左右，再判断谁是 0；两边都有才取 min
#   - 只有 not root.left and not root.right 才是叶子
class Solution(object):
    def minDepth(self, root):
        if not root:
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if not left:
            return right+1
        if not right:
            return left + 1
        if left and right:
            return min(right,left)+1

# === 第29题：完全二叉树节点数（#222） ===
# 题目：给定完全二叉树，返回节点个数
# 示例：[1,2,3,4,5,6] → 6
# 易错点：
#   - 求最左深度（一直往左）和最右深度（一直往右）
#   - 相等 → 满二叉树，返回 2^h - 1
#   - 不等 → 递归 1 + 左 + 右
class Solution(object):
    def countNodes(self, root):
        if not root:
            return 0
        node = root
        depth_left = 0
        while node:            
            depth_left +=1
            node = node.left

        node = root
        depth_right = 0
        while node:      
            
            depth_right +=1
            node = node.right

        if depth_left==depth_right:
            return 2**depth_left-1

        return self.countNodes(root.left)+self.countNodes(root.right)+1
        
            

# === 第30题：翻转二叉树（#226） ===
# 题目：给定二叉树，翻转它（每个节点的左右子树互换）
# 示例：[4,2,7,1,3,6,9] → [4,7,2,9,6,3,1]
# 易错点：
#   - 交换的是左右子树，不是节点的值
#   - root.left, root.right = root.right, root.left 一行搞定
#   - 递归：先交换再递归，或先递归再交换都行
#   - 空树返回 None
class Solution(object):
    def invertTree(self, root):
        if not root:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

# === 第31题：平衡二叉树（#110） ===
# 题目：判断二叉树是否平衡（每个节点左右高度差≤1）
# 示例：[3,9,20,null,null,15,7] → True
# 易错点：
#   - check返回高度，不平衡返回-1
#   - 空树返回0（不是True/False）
#   - 主函数判断 check(root) != -1
class Solution(object):
    def isBalanced(self, root):
        def check(root):
            if not root:
                return 0
            left = check(root.left)
            right = check(root.right)
            if left == -1 or right == -1:
                return -1
            if abs(left-right) > 1:
                return -1
            else:
                return max(left,right)+1
        return check(root) != -1

# === 第32题：对称二叉树（#101） ===
# 题目：判断二叉树是否镜像对称
# 示例：[1,2,2,3,4,4,3] → True；[1,2,2,null,3,null,3] → False
# 易错点：
#   - 辅助函数 compare(left, right) 比较两个子树
#   - 左的左 vs 右的右，左的右 vs 右的左
#   - 两个都空→True，一个空→False，值不等→False
class Solution(object):
    def isSymmetric(self, root):
        def compare(left,right):
            if not left and not right:
                return True
            elif left or right:
                return False
            elif left.val != right.val:
                return False
            return compare(left.left,right.right) and compare(left.right,right.left)
        return compare(root.left,root.right)

# === 第33题：二叉树所有路径（#257） ===
# 题目：返回所有从根到叶子的路径，用"->"连接
# 示例：[1,2,3,null,5] → ["1->2->5", "1->3"]
# 易错点：
#   - 回溯：append → 递归 → pop
#   - 叶子节点用 "->".join(path) 记录
#   - 空树返回空列表
class Solution(object):
    def binaryTreePaths(self, root):
        result = []
        def dfs(node,path):
            if not node:
                return
            path.append(str(node.val))
            if not node.left and not node.right:
                result.append("->".join(path))
            dfs(node.left,path)
            dfs(node.right,path)

            path.pop()
        dfs(root,[])
        return result

# === 第34题：完全二叉树节点数（#222） ===
# 题目：给定完全二叉树，返回节点个数
# 示例：[1,2,3,4,5,6] → 6
# 易错点：
#   - 求最左深度（一直往左）和最右深度（一直往右）
#   - 相等 → 满二叉树，返回 2^h - 1
#   - 不等 → 递归 1 + 左 + 右
class Solution(object):
    def countNodes(self, root):
        if not root:
            return 0

        node = root
        left_depth = 0
        while node:
            left_depth += 1
            node = node.left

        node = root
        right_depth = 0
        while node:
            right_depth += 1
            node = node.right

        if left_depth == right_depth:
            return 2**left_depth - 1

        return self.countNodes(root.left)+self.countNodes(root.right)+1

# === 第35题：左叶子之和（#404） ===
# 题目：返回所有左叶子节点的值之和
# 示例：[3,9,20,null,null,15,7] → 24（9+15）
# 易错点：
#   - 左叶子 = 是父节点的左孩子 + 是叶子（没子节点）
#   - 用 is_left 参数标记是否是左孩子
#   - 根节点不是任何节点的左孩子，传 False
class Solution(object):
    def sumOfLeftLeaves(self, root):
        def dfs(node,is_left):
            if not node:
                return 0
            if is_left and not node.left and not node.right:
                return node.val
            return dfs(node.left,True) + dfs(node.right,False)
        return dfs(root,False)

# === 第36题：平衡二叉树（#110） ===
# 题目：判断二叉树是否平衡（每个节点左右高度差≤1）
# 示例：[3,9,20,null,null,15,7] → True
# 易错点：
#   - check返回高度，不平衡返回-1
#   - 空树返回0（不是True/False）
#   - 主函数判断 check(root) != -1
class Solution(object):
    def isBalanced(self, root):
        def check(node):
            if not node:
                return 0
            left = check(node.left)
            right = check(node.right)

            if left == -1 or right ==-1:
                return -1
            if abs(left-right)>1:
                return -1
            return max(left,right)+1
        return check(root) != -1

# === 第37题：找树左下角值（#513） ===
# 题目：找到二叉树最后一层最左边的节点值
# 示例：[2,1,3] → 1；[1,2,3,4,null,5,6,null,null,7] → 7
# 易错点：
#   - BFS层序遍历，每层第一个节点(i==0)就是最左边
#   - 别忘了把子节点加入队列
#   - 最后一层循环结束时的result就是答案
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

# === 第38题：二叉树所有路径（#257） ===
# 题目：返回所有从根到叶子的路径，用"->"连接
# 示例：[1,2,3,null,5] → ["1->2->5", "1->3"]
# 易错点：
#   - 回溯：append → 递归 → pop
#   - 叶子节点用 "->".join(path) 记录
#   - 空树返回空列表
class Solution(object):
    def binaryTreePaths(self, root):
        result = []
        def dfs(node,path):
            if not node:
                return             
            path.append(str(node.val))
            if not node.left and not node.right:
                result.append("->".join(path))
            dfs(node.left,path)
            dfs(node.right,path)

            path.pop()
        dfs(root,[])
        return result

# === 第39题：从前序与中序遍历构造二叉树（#105） ===
# 题目：给前序 preorder 和中序 inorder，构造二叉树返回根
# 示例：preorder=[3,9,20,15,7], inorder=[9,3,15,20,7] → [3,9,20,null,null,15,7]
# 易错点：
#   - 前序第一个 = 根
#   - inorder.index(根) = 左子树节点个数 idx
#   - 前序：preorder[1:idx+1] / preorder[idx+1:]
#   - 中序：inorder[:idx] / inorder[idx+1:]
#   - 空数组返回 None
Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        if not preorder:
            return None
        root_val = preorder[0]
        root = TreeNode(root_val)

        idx = inorder.index(root_val)

        left_pre = preorder[1:idx+1]
        right_pre = preorder[idx+1:]
        left_in = inorder[0:idx]
        right_in = inorder[idx+1:]

        root.left = self.buildTree(left_pre,left_in)
        root.right = self.buildTree(right_pre,right_in)

        return root




# === 第40题：路径总和（#112） ===
# 题目：判断是否存在根到叶子的路径，节点和等于 targetSum
# 示例：[5,4,8,11,null,13,4,7,2,null,null,null,1], target=22 → True
# 易错点：
#   - 必须到叶子节点才算
#   - 回溯：append 和 pop 必须成对，叶子 return 前也要 pop
#   - 返回 left or right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        if not root:
            return False
        def dfs(node,path):
            if not node:
                return False
            path.append(node.val)
            if not node.left and not node.right:
                res = (sum(path) == targetSum)
                path.pop()
                return res

            left = dfs(node.left,path)
            right = dfs(node.right,path)
            path.pop()
            return left or right

        return dfs(root,[])

# === 第41题：从中序与后序遍历构造二叉树（#106） ===
# 题目：给中序 inorder 和后序 postorder，构造二叉树返回根
# 示例：inorder=[9,3,15,20,7], postorder=[9,15,7,20,3] → [3,9,20,null,null,15,7]
# 易错点：
#   - 后序「左→右→根」，最后一个是根
#   - inorder.index(根)=左子树大小 idx
#   - 后序：postorder[:idx] / postorder[idx:-1]（右子树别带根）
#   - 中序：inorder[:idx] / inorder[idx+1:]
class Solution(object):
    def buildTree(self, inorder, postorder):
        if not inorder:
            return None
        root_val = postorder[-1]
        root = TreeNode(root_val)

        idx = inorder.index(root_val)

        left_in = inorder[:idx]
        right_in = inorder[idx+1:]

        left_post = postorder[:idx]
        right_post = postorder[idx:-1]

        root.left = self.buildTree(left_in,left_post)
        root.right = self.buildTree(right_in,right_post)

        return root
# === 第42题：二叉树所有路径（#257） ===
# 题目：返回所有从根到叶子的路径，用"->"连接
# 示例：[1,2,3,null,5] → ["1->2->5", "1->3"]
# 易错点：
#   - 回溯：append → 递归 → pop
#   - 叶子节点用 "->".join(path) 记录
#   - 空树返回空列表
class Solution(object):
    def binaryTreePaths(self, root):
        if not root:
            return []
        result = []
        def dfs(node,path):
            if not node:
                return 
            path.append(str(node.val))
            if not node.left and not node.right:
                result.append("->".join(path))
                
            dfs(node.left,path)
            dfs(node.right,path)
            path.pop()
        dfs(root,[])
        return result

# === 第43题：最大二叉树（#654） ===
# 题目：给不重复数组 nums，最大值当根，左右分别递归构造最大二叉树
# 示例：[3,2,1,6,0,5] → [6,3,5,null,2,0,null,null,1]
# 易错点：
#   - max(nums) 是根，nums.index(max_val) 切两刀
#   - 嵌套函数直接调用，别加 self
#   - 空数组返回 None（内层也要判）
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

# === 第44题：从前序与中序遍历构造二叉树（#105） ===
# 题目：给前序 preorder 和中序 inorder，构造二叉树返回根
# 示例：preorder=[3,9,20,15,7], inorder=[9,3,15,20,7] → [3,9,20,null,null,15,7]
# 易错点：
#   - 前序第一个 = 根
#   - inorder.index(根) = 左子树节点个数 idx
#   - 前序：preorder[1:idx+1] / preorder[idx+1:]
#   - 中序：inorder[:idx] / inorder[idx+1:]
class Solution(object):
    def buildTree(self, preorder, inorder):
        if not preorder:
            return None
        root_val = preorder[0]
        root = TreeNode(root_val)
        idx = inorder.index(root_val)

        left_pre = preorder[1:idx+1]
        right_pre = preorder[idx+1:]
        left_in = inorder[0:idx]
        right_in = inorder[idx+1:]

        root.left = self.buildTree(left_pre,left_in)
        root.right = self.buildTree(right_pre,right_in)

        return root

# === 第45题：合并二叉树（#617） ===
# 题目：两棵二叉树合并，重叠的节点值相加
# 示例：root1=[1,3,2,5], root2=[2,1,3,null,4,null,7] → [3,4,5,5,4,null,7]
# 易错点：
#   - 都空 → None
#   - 只一边有 → 直接返回那一边（不用新建）
#   - 都有 → 新建节点，值相加，递归左右
class Solution(object):
    def mergeTrees(self, root1, root2):
        if not root1 and not root2:
            return None
        if not root1:
            return root2
        if not root2:
            return root1
        root = TreeNode(root1.val+root2.val)
        root.left = self.mergeTrees(root1.left,root2.left)
        root.right = self.mergeTrees(root1.right,root2.right)
        return root


# === 第46题：二叉搜索树中的搜索（#700） ===
# 题目：在 BST 中找值为 val 的节点，返回以它为根的子树
# 示例：root=[4,2,7,1,3], val=2 → [2,1,3]
# 易错点：
#   - BST 左小右大：val < root.val 往左，val > root.val 往右
#   - 相等 → 返回该节点；走到空 → 返回 None
#   - 每个分支都要 return
class Solution(object):
    def searchBST(self, root, val):
        if not root:
            return None
        if val == root.val:
            return root
        if val > root.val:
            return self.searchBST(root.right,val)
        if val < root.val:
            return self.searchBST(root.left,val)

# === 第47题：验证二叉搜索树（#98） ===
# 题目：判断一棵二叉树是不是合法 BST
# 示例：[5,1,4,null,null,3,6] → False
# 易错点：
#   - 不能只比当前节点和左右孩子，要传上下界
#   - 左孩子上界收紧成 node.val，右孩子下界收紧成 node.val
#   - 初始边界用 float('-inf') / float('inf')
class Solution(object):
    def isValidBST(self, root):
        if not root:
            return True
        def check(node,low,high):
            if not node:
                return True
            if node.val > high or node.val < low:
                return False
            return check(node.left,low,node.val) and check(node.right,node.val,high)
        return check(root,float('-inf'),float('inf'))

# === 第48题：路径总和（#112） ===
# 题目：判断是否存在根到叶子的路径，节点和等于 targetSum
# 示例：[5,4,8,11,null,13,4,7,2,null,null,null,1], target=22 → True
# 易错点：
#   - 必须到叶子节点才算
#   - 回溯：append 和 pop 必须成对，叶子 return 前也要 pop
#   - 返回 left or right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        if not root:
            return False
        def dfs(node,path):
            if not node:
                return False
            path.append(node.val)
            
            if not node.left and not node.right:                
                res = sum(path) == targetSum
                path.pop()
                return res
            left = dfs(node.left,path)
            right = dfs(node.right,path)
            path.pop()
            return  left or right

        return dfs(root,[])

# === 第49题：二叉搜索树的最小绝对差（#530） ===
# 题目：返回 BST 任意两节点值之差的最小绝对值
# 示例：[4,2,6,1,3] → 1
# 易错点：
#   - BST 中序遍历是递增的 → 最小差一定在相邻节点之间
#   - 用共享列表收集，别在函数里新建列表
#   - 用单独变量存最小差，别覆盖列表
class Solution(object):
    def getMinimumDifference(self, root):
        if not root:
            return 0
        result = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)
        diff = float('inf')
        inorder(root)
        for i in range(len(result)-1):
            diff = min(diff,result[i+1]-result[i])
        return diff


# === 第50题：合并二叉树（#617） ===
# 题目：两棵二叉树合并，重叠的节点值相加
# 示例：root1=[1,3,2,5], root2=[2,1,3,null,4,null,7] → [3,4,5,5,4,null,7]
# 易错点：
#   - 都空 → None
#   - 只一边有 → 直接返回那一边（不用新建）
#   - 都有 → 新建节点，值相加，递归左右
class Solution(object):
    def mergeTrees(self, root1, root2):
        if not root1 and not root2:
            return None
        if not root1:return root2
        if not root2:return root1
        root = TreeNode(root1.val + root2.val)
        root.left = self.mergeTrees(root1.left,root2.left)
        root.right = self.mergeTrees(root1.right,root2.right)
        return root

# === 第51题：二叉搜索树中的众数（#501） ===
# 题目：给有重复值的 BST，返回所有众数（出现次数最多的值）
# 示例：[1,null,2,2] → [2]
# 易错点：
#   - 中序遍历收集所有值，用 Counter 统计
#   - 返回所有「次数 == 最大次数」的值
#   - 别忘了 import: from collections import Counter
from collections import Counter
class Solution(object):
    def findMode(self, root):
        # 在这里默写
        if not root:
            return []
        result = []
        def inorder(node):
           if not node:
               return
           inorder(node.left)
           result.append(node.val)
           inorder(node.right)
        inorder(root)
        answer = []
        res = Counter(result)
        max_count = max(res.values())
        for k,v in res.items():
            if v == max_count:
                answer.append(k)
        return answer

        
         

# === 第52题：验证二叉搜索树（#98） ===
# 题目：判断一棵二叉树是不是合法 BST
# 示例：[5,1,4,null,null,3,6] → False
# 易错点：
#   - 不能只比当前节点和左右孩子，要传上下界
#   - 左孩子上界收紧成 node.val，右孩子下界收紧成 node.val
#   - 初始边界用 float('-inf') / float('inf')
class Solution(object):
    def isValidBST(self, root):
        if not root:
            return True
        def check(node,low,high):
            if not node:
                return True
            if not (low < node.val < high):
                return False
            left = check(node.left,low,node.val)
            right = check(node.right,node.val,high)
            return left and right
        return check(root,float('-inf'),float('inf'))

# === 第53题：二叉树的最近公共祖先（#236） ===
# 题目：给节点 p、q，找它们的最近公共祖先（LCA）
# 示例：root=[3,5,1,6,2,0,8,null,null,7,4], p=5, q=1 → 3
# 易错点：
#   - 基准：空 或 当前节点是 p/q → 返回当前节点
#   - 左右都非空 → 当前节点就是 LCA
#   - 只有一边非空 → 把那一边传上去
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)
        if left and right:
            return root
        return left if left else right
        

# === 第54题：二叉搜索树中的搜索（#700） ===
# 题目：在 BST 中找值为 val 的节点，返回以它为根的子树
# 示例：root=[4,2,7,1,3], val=2 → [2,1,3]
# 易错点：
#   - BST 左小右大：val < root.val 往左，val > root.val 往右
#   - 相等 → 返回该节点；走到空 → 返回 None
#   - 每个分支都要 return，参数别漏 val
class Solution(object):
    def searchBST(self, root, val):
        if not root or root.val == val:
            return root
        if val > root.val:
           return self.searchBST(root.right,val)
        elif val < root.val:
           return self.searchBST(root.left,val)

# === 第55题：二叉搜索树的最近公共祖先（#235） ===
# 题目：给 BST 和节点 p、q，找最近公共祖先
# 示例：root=[6,2,8,0,4,7,9,null,null,3,5], p=2, q=8 → 6
# 易错点：
#   - p、q 是节点，比较用 p.val / q.val
#   - 都小于 root → 往左；都大于 root → 往右
#   - 否则（分居两侧）→ root 就是 LCA
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if not root or root == p or root == q:
            return root
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left,p,q)
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right,p,q)
        return root
        

# === 第56题：二叉搜索树中的众数（#501） ===
# 题目：给有重复值的 BST，返回所有众数
# 示例：[1,null,2,2] → [2]
# 易错点：
#   - 中序遍历收集所有值，用 Counter 统计
#   - 返回所有「次数 == 最大次数」的值
#   - 别忘了 from collections import Counter
from collections import Counter
class Solution(object):
    def findMode(self, root):
        if not root:
            return []
        vals = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            vals.append(root.val)
            inorder(root.right)
        inorder(root)
        result = Counter(vals)
        max_val = max(result.values())
        res = []
        for k,v in result.items():
            if v==max_val:
                res.append(k)
        return res

# === 第57题：二叉搜索树中的插入操作（#701） ===
# 题目：往 BST 插入一个值，返回根节点
# 示例：root=[4,2,7,1,3], val=5 → [4,2,7,1,3,5]
# 易错点：
#   - 空节点 = 插入位置 → 新建节点返回
#   - val < root.val 往左，> 往右
#   - 递归结果必须接回 root.left / root.right
class Solution(object):
    def insertIntoBST(self, root, val):
        if not root:
            return TreeNode(val)
        if root.val > val:
            root.left = self.insertIntoBST(root.left,val)
        if root.val < val:
            root.right = self.insertIntoBST(root.right,val)
        return root

# === 第58题：二叉树的最近公共祖先（#236） ===
# 题目：给节点 p、q，找它们的最近公共祖先（LCA）
# 示例：root=[3,5,1,6,2,0,8,null,null,7,4], p=5, q=1 → 3
# 易错点：
#   - 基准：空 或 当前节点是 p/q → 返回当前节点
#   - 左右都非空 → 当前节点就是 LCA
#   - 只有一边非空 → 把那一边传上去
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)
        if left and right:
            return root
        return left if left else right

# === 第59题：删除二叉搜索树中的节点（#450） ===
# 题目：删掉 BST 中值为 key 的节点，返回根节点
# 示例：root=[5,3,6,2,4,null,7], key=3 → [5,4,6,2,null,null,7]
# 易错点：
#   - 5种情况：没找到/叶子/只有右/只有左/两个都有
#   - 两个都有：右子树最小值（一直往左）覆盖当前值，再递归删它
#   - 递归结果接回 root.left/right，最后 return root
class Solution(object):
    def deleteNode(self, root, key):
        # 在这里默写
        pass

# === 第60题：二叉搜索树的最近公共祖先（#235） ===
# 题目：给 BST 和节点 p、q，找最近公共祖先
# 示例：root=[6,2,8,0,4,7,9,null,null,3,5], p=2, q=8 → 6
# 易错点：
#   - p、q 是节点，比较用 p.val / q.val
#   - 都小于 root → 往左；都大于 root → 往右
#   - 否则（分居两侧）→ root 就是 LCA
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        # 在这里默写
        pass

# === 第61题：修剪二叉搜索树（#669） ===
# 题目：修剪 BST，使所有节点值都在 [low, high] 内
# 示例：root=[1,0,2], low=1, high=2 → [1,null,2]
# 易错点：
#   - 根<low → 左子树全<low，扔左看右
#   - 根>high → 右子树全>high，扔右看左
#   - 在范围内 → 保留根，递归修剪左右
#   - 空树返回 None（不是[]）
class Solution(object):
    def trimBST(self, root, low, high):
        # 在这里默写
        pass

# === 第62题：二叉搜索树中的插入操作（#701） ===
# 题目：往 BST 插入一个值，返回根节点
# 示例：root=[4,2,7,1,3], val=5 → [4,2,7,1,3,5]
# 易错点：
#   - 空节点 = 插入位置 → 新建节点返回
#   - val < root.val 往左，> 往右
#   - 递归结果必须接回 root.left / root.right
class Solution(object):
    def insertIntoBST(self, root, val):
        # 在这里默写
        pass
