"""
LeetCode #283 - Move Zeroes
Difficulty: Easy
Topics: Array, Two Pointers
Date: 2026-09-27
Time spent: 30 min
Status: Solved

## Problem Statement
Given an integer array nums, move all 0's to the end of it while maintaining
the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]

## Idea
Use two pointers. j tracks where the next non-zero element should go.
Iterate i through nums: when nums[i] != 0, copy it to nums[j] and
increment j. After the loop, all positions from j to end are filled with 0.

## Complexity
- Time: O(n) one pass to move non-zeroes + one pass to fill zeroes
- Space: O(1) in-place modification only

## Submission Log
- [x] Submitted on LeetCode
- [x] Passed all test cases
"""


# ============================================================
# LeetCode Submission (copy entire block to LeetCode)
# ============================================================

class Solution:
    def moveZeroes(self, nums):
       j = 0
       for i in range(len(nums)):
           if nums[i] != 0:
               nums[j] = nums[i]
               j += 1
       for k in range(j,len(nums)):
            nums[k] = 0

               
               
