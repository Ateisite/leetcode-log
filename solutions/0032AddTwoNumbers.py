"""
LeetCode #2 - Add Two Numbers
Difficulty: Medium
Topics: Linked List, Math
Date: 2026-10-23
Time spent: 30 min
Status: Solved

## Problem Statement
Given two non-empty linked lists representing two non-negative integers.
Digits are stored in reverse order. Add the two numbers and return the
sum as a linked list.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

## Idea
Simulate elementary school addition on reversed linked lists. Use dummy
head + current pointer to build result list. Each round: sum both digits
plus carry, create node with sum%10, update carry=sum//10. Handle unequal
lengths with `val if node else 0`. Loop continues while either list has
nodes OR carry is non-zero (final carry creates new node).

## Complexity
- Time: O(max(m, n)) — single pass through both lists
- Space: O(max(m, n)) — result list

## Submission Log
- [x] Submitted on LeetCode
- [x] Passed all test cases
"""


# ============================================================
# LeetCode Submission (copy entire block to LeetCode)
# ============================================================

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
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