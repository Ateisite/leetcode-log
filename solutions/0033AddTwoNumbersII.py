"""
LeetCode #445 - Add Two Numbers II
Difficulty: Medium
Topics: Linked List, Math, Stack
Date: 2026-10-24
Time spent: 25 min
Status: Solved

## Problem Statement
Given two non-empty linked lists representing two non-negative integers.
The most significant digit comes first. Add the two numbers and return
the sum as a linked list.

Example 1:
Input: l1 = [7,2,4,3], l2 = [5,6,4]
Output: [7,8,0,7]
Explanation: 7243 + 564 = 7807

Example 2:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [8,0,7]

Example 3:
Input: l1 = [0], l2 = [0]
Output: [0]

## Idea
Reverse both input lists, then reuse #2's addTwoNumbers logic (digits
in reverse order), then reverse the result. Three steps:
reverse → add → reverse. Reuses previously solved sub-problems.

## Complexity
- Time: O(m + n) — three linear passes (two reverses + one add + one reverse)
- Space: O(max(m, n)) — result list

## Submission Log
- [x] Submitted on LeetCode
- [x] Passed all test cases
"""


# ============================================================
# LeetCode Submission (copy entire block to LeetCode)
# ============================================================
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        reverse = ListNode()
        while head:
            next_node = head.next
            head.next = reverse.next
            reverse.next = head
            head = next_node
        return reverse.next

    def addTwoNumbers1(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        current = dummy
        sum = 0
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            sum = v1 + v2 + carry
            current.next = ListNode(sum % 10)
            carry = sum //10 
            current = current.next
            if l1:l1 = l1.next
            if l2:l2 = l2.next
        return dummy.next

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        l1 = self.reverseList(l1)
        l2 = self.reverseList(l2)
        result = self.addTwoNumbers1(l1,l2)
        return self.reverseList(result)
