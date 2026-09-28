"""
LeetCode #66 - Plus One
Difficulty: Easy
Topics: Array, Math
Date: 2026-09-28
Time spent: 25 min
Status: Solved

## Problem Statement
You are given a large integer represented as an integer array digits, where
each digits[i] is the ith digit of the integer. The digits are ordered from
most significant to least significant in left-to-right order. The large
integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

Example 1:
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

Example 2:
Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].

Example 3:
Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].

## Idea
Traverse from the last digit backwards. If the current digit is less than 9,
just add 1 and return immediately (no carry needed). If it is 9, adding 1
makes 10, so set it to 0 and let the loop continue to carry into the next
digit. If the loop finishes without returning, every digit was 9, so the
result is [1] followed by all zeros.

## Complexity
- Time: O(n) at most one pass through the digits
- Space: O(1) in-place except the all-9s case which needs a new array

## Submission Log
- [x] Submitted on LeetCode
- [x] Passed all test cases
"""


# ============================================================
# LeetCode Submission (copy entire block to LeetCode)
# ============================================================

class Solution(object):
    def plusOne(self, digits):
      for i in range(len(digits) - 1, -1, -1):    # 从最后一位往前
        if digits[i] < 9:                        # 不是 9
            digits[i] += 1                       # 直接加 1
            return digits                        # 结束！
        digits[i] = 0                            # 是 9，变 0，继续循环

    # 循环走完还没 return → 全是 9
      return [1] + digits 


      
        