"""
复习默写 — 白纸写，不看笔记
写完让 Claude 对照
"""

# === 第1题：反转链表（#206） ===
# 在这里从零写 reverseList

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


