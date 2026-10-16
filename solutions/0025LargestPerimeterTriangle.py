"""
LeetCode #976 - Largest Perimeter Triangle
Difficulty: Easy
Topics: Array, Math, Sorting
Date: 2026-10-16
Time spent: 15 min
Status: Solved

## Problem Statement
Given an integer array nums, return the largest perimeter of a triangle
with non-zero area, formed from three of these lengths. If impossible,
return 0.

Example 1:
Input: nums = [2,1,2]
Output: 5

Example 2:
Input: nums = [1,2,1,10]
Output: 0

## Idea
Sort descending. Check adjacent triplets: if the largest side is less than
the sum of the other two, they form a valid triangle. First valid triplet
gives the largest perimeter (greedy).

## Complexity
- Time: O(n log n) — sorting dominates
- Space: O(1) — in-place sort

## Submission Log
- [x] Submitted on LeetCode
- [x] Passed all test cases
"""


# ============================================================
# LeetCode Submission (copy entire block to LeetCode)
# ============================================================

class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse=True)
        for i in range(len(nums)-2):
            if nums[i]<nums[i+1]+nums[i+2]:
                return nums[i]+nums[i+1]+nums[i+2]
        return 0
