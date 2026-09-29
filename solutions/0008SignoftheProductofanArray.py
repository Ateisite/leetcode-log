"""
LeetCode #1822 - Sign of the Product of an Array
Difficulty: Easy
Topics: Array, Math
Date: 2026-09-29
Time spent: 15 min
Status: Solved

## Problem Statement
Implement a function signFunc(x) that returns:
- 1 if x is positive.
- -1 if x is negative.
- 0 if x is equal to 0.

You are given an integer array nums. Let product be the product of all
values in the array nums.

Return signFunc(product).

Example 1:
Input: nums = [-1,-2,-3,-4,3,2,1]
Output: 1
Explanation: The product of all values in the array is 144, and signFunc(144) = 1

Example 2:
Input: nums = [1,5,0,2,-3]
Output: 0
Explanation: The product of all values in the array is 0, and signFunc(0) = 0

Example 3:
Input: nums = [-1,1,-1,1,-1]
Output: -1
Explanation: The product of all values in the array is -1, and signFunc(-1) = -1

## Idea
No need to compute the actual product. Traverse the array: if any element
is 0, return 0 immediately. Otherwise count the number of negative numbers.
If the count is even, the product is positive (return 1); if odd, the
product is negative (return -1).

## Complexity
- Time: O(n) single pass through the array
- Space: O(1) only a counter variable

## Submission Log
- [x] Submitted on LeetCode
- [x] Passed all test cases
"""


# ============================================================
# LeetCode Submission (copy entire block to LeetCode)
# ============================================================

class Solution(object):
    def arraySign(self, nums):
       count = 0
       for i in range(len(nums)):
          if nums[i] == 0 :
           return 0
          if nums[i] < 0 :
               count += 1
       if count % 2 != 0:
          return -1
       else :
          return 1
        