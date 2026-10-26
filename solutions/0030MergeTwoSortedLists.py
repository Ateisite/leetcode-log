"""
LeetCode #21 - Merge Two Sorted Lists
Difficulty: Easy
Topics: Linked List, Two Pointers
Date: 2026-10-21
Time spent: 30 min
Status: Solved

## Problem Statement
Merge two sorted linked lists into one sorted list. The list should be
made by splicing together the nodes of the first two lists.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]

Constraints:
- The number of nodes in both lists is in the range [0, 50].
- -100 <= Node.val <= 100
- Both list1 and list2 are sorted in non-decreasing order.

## Idea
Use a dummy head node to avoid edge cases for the first comparison.
Traverse both lists with node references (not indices): compare current
nodes, append the smaller one to result, advance that pointer.
When one list is exhausted, attach the remaining tail of the other list.

## Complexity
- Time: O(m + n) — each node visited exactly once
- Space: O(1) — only pointers, no new nodes created

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
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()        
        current  = dummy
        while list1 and list2:
            if list1.val<=list2.val:
                current.next = list1
                current = current.next
                list1 = list1.next                
            else:
                current.next = list2
                current = current.next
                list2 = list2.next
        current.next = list1 if list1 else list2
        return dummy.next
        



