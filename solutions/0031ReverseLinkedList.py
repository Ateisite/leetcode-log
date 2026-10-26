"""
LeetCode #206 - Reverse Linked List
Difficulty: Easy
Topics: Linked List
Date: 2026-10-22
Time spent: 20 min
Status: Solved

## Problem Statement
Given the head of a singly linked list, reverse the list, and return
the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []

## Idea
Head insertion (头插法). Create a dummy head for the new list.
Walk through original list: for each node, save its next, insert it
after dummy (reverse.next), then advance. Each node becomes the new
front of the reversed list.

## Complexity
- Time: O(n) — single pass through all nodes
- Space: O(1) — only pointers, no new nodes (dummy is just a placeholder)

## Submission Log
- [x] Submitted on LeetCode
- [x] Passed all test cases
"""


# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
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

        

