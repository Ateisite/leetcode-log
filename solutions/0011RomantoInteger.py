"""
LeetCode #13 - Roman to Integer
Difficulty: Easy
Topics: Hash Table, String, Math
Date: 2026-10-02
Time spent: 30 min
Status: Solved

## Problem Statement
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II, 12 as XII, 27 as XXVII.

Roman numerals are usually written largest to smallest from left to right.
However, the numeral for four is IV (subtraction). The same principle applies
to IX (9), XL (40), XC (90), CD (400), CM (900).

Given a roman numeral, convert it to an integer.

Example 1:
Input: s = "III"
Output: 3

Example 2:
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V = 5, III = 3.

Example 3:
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90, IV = 4.

## Idea
Use a dictionary to map each Roman symbol to its value. Traverse the string
from left to right (except the last character). Compare the current symbol's
value with the next one: if current >= next, add it; otherwise subtract it.
Finally, add the value of the last character. This handles subtraction cases
like IV (4), IX (9), XL (40), etc.

## Complexity
- Time: O(n) single pass where n = len(s)
- Space: O(1) dictionary has fixed 7 entries

## Submission Log
- [x] Submitted on LeetCode
- [x] Passed all test cases
"""


# ============================================================
# LeetCode Submission (copy entire block to LeetCode)
# ============================================================

class Solution(object):
    def romanToInt(self, s):
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        k = 0
        for i in range(len(s)-1):
            if roman[s[i]] >= roman[s[i+1]]:
                k = k + roman[s[i]]
            else:
                k = k - roman[s[i]]
        k = k + roman[s[len(s)-1]]
        return k 


