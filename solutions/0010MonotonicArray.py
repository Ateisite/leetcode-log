"""
LeetCode #896 - Monotonic Array
Difficulty: Easy
Topics: Array
Date: 2026-10-01
Time spent: 25 min
Status: Solved

## Problem Statement
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j].
An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

Given an integer array nums, return true if the given array is monotonic,
or false otherwise.

Example 1:
Input: nums = [1,2,2,3]
Output: true

Example 2:
Input: nums = [6,5,4,4]
Output: true

Example 3:
Input: nums = [1,3,2]
Output: false

## Idea
Use two boolean flags: increasing and decreasing. Traverse the array once.
If nums[i] < nums[i+1], set increasing = True. If nums[i] > nums[i+1],
set decreasing = True. If both flags become True at any point, the array
is not monotonic, return False. If the loop finishes without both flags
being True, return True.

## Complexity
- Time: O(n) single pass
- Space: O(1) only two boolean variables

## Submission Log
- [x] Submitted on LeetCode
- [x] Passed all test cases
"""


# ============================================================
# LeetCode Submission (copy entire block to LeetCode)
# ============================================================

class Solution(object):
    def isMonotonic(self, nums):
       increasing = False
       decreasing = False
       for i in range(len(nums) - 1):
            if nums[i] < nums[i+1]:
                increasing = True
            if nums[i] > nums[i+1]:
                decreasing = True
            if increasing and decreasing:
                return False
       return True

