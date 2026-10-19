"""
LeetCode #43 - Multiply Strings
Difficulty: Medium
Topics: String, Math
Date: 2026-10-19
Time spent: 45 min
Status: Solved

## Problem Statement
Given two non-negative integers num1 and num2 represented as strings,
return the product as a string. Must not use BigInteger or convert to
integer directly.

Example 1:
Input: num1 = "2", num2 = "3"
Output: "6"

Example 2:
Input: num1 = "123", num2 = "456"
Output: "56088"

## Idea
Simulate manual multiplication using an array. For each digit pair
(num1[i], num2[j]), multiply and add to position (i+j, i+j+1). Handle
carry by adding pos[p2]//10 to the higher position and keeping
pos[p2]%10 in the lower position. Finally strip leading zeros and join.

## Complexity
- Time: O(m * n) — nested loops over both strings
- Space: O(m + n) — result array

## Submission Log
- [x] Submitted on LeetCode
- [x] Passed all test cases
"""


# ============================================================
# LeetCode Submission (copy entire block to LeetCode)
# ============================================================

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        m, n= len(num1), len(num2)
        pos = [0]*(m+n)
        mul = 0
        p1, p2 = 0 ,0

        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                mul = int(num1[i])*int(num2[j])
                p1 = i + j + 1
                p2 = i + j
                pos[p1] += mul

                pos[p2] += pos[p1] // 10
                pos[p1] = pos[p1] % 10
        result = []

        for n in pos:
           if not (len(result) == 0 and n == 0): 
               result.append(str(n))
        result = ''.join(result)
        return result if result else "0" 


                
