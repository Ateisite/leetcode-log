"""
LeetCode #67 - Add Binary
Difficulty: Easy
Topics: String, Math, Bit Manipulation
Date: 2026-10-18
Time spent: 30 min
Status: Solved

## Problem Statement
Given two binary strings a and b, return their sum as a binary string.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"

## Idea
Simulate binary addition with carry. Use two pointers starting from the
end of each string, moving left. Add digits along with carry, append
result bit (total % 2), update carry (total // 2). Reverse and join at
the end.

## Complexity
- Time: O(max(m, n)) — single pass through the longer string
- Space: O(max(m, n)) — for the result list

## Submission Log
- [x] Submitted on LeetCode
- [x] Passed all test cases
"""


# ============================================================
# LeetCode Submission (copy entire block to LeetCode)
# ============================================================

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i = len(a)-1
        j = len(b)-1
        result = []
        carry = 0
        while i >= 0 or j >= 0 or carry:
            total = carry
            if i >= 0 :
                total += int(a[i])
                i -= 1
            if j >= 0 :
                total += int(b[j])
                j -= 1
            result.append(str(total%2))
            carry = total // 2
        return ''.join(reversed(result))

            