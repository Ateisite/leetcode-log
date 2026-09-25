"""
LeetCode #242 - Valid Anagram
Difficulty: Easy
Topics: String, Hash Table, Sorting
Date: 2026-09-25
Time spent: [X] min
Status: [Solved / Looked at solution / Timeout]

## Problem Statement
Given two strings s and t, return true if t is an anagram of s, and false
otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:
1 <= s.length, t.length <= 5 * 10^4
s and t consist of lowercase English letters.

Follow up: What if the inputs contain Unicode characters? How would you adapt
your solution to such a case?

## Idea
First check if lengths differ (if so, not anagrams). Then use Counter to
count character frequencies in both strings. Iterate through count_s and
return False immediately if any count differs. If all match, return True.

## Complexity
- Time: O(n) where n = len(s)
- Space: O(n) for the two Counter objects

## Submission Log
- [x] Submitted on LeetCode
- [x] Passed all test cases
"""


# ============================================================
# LeetCode Submission (copy entire block to LeetCode)
# ============================================================

from collections import Counter

class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        count_s = Counter(s)
        count_t = Counter(t)
        for char in count_s:
            if count_t[char] != count_s[char]:
                return False
        return True
        #return count_s == count_t


