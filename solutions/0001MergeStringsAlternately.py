"""
LeetCode #1768 - Merge Strings Alternately
Difficulty: Easy
Topics: Two Pointers, String
Date: 2026-09-22
Time spent: 30 min
Status: Solved

## Problem Statement
You are given two strings word1 and word2. Merge the strings by adding
letters in alternating order, starting with word1. If a string is longer
than the other, append the additional letters onto the end of the merged
string.

Return the merged string.

Example 1:
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"

Example 2:
Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"

Constraints:
1 <= word1.length, word2.length <= 100
word1 and word2 consist of lowercase English letters.

## Idea
Iterate through the maximum length of both strings. At each index, append
word1[i] if it exists, then append word2[i] if it exists. When the shorter
string is exhausted, the `if` check fails and it is automatically skipped.

## Complexity
- Time: O(n) where n = max(len(word1), len(word2))
- Space: O(1) extra space (not counting the output string)
"""



def merge_alternately(word1,word2):
    i = 0
    result = ""
    for i in range(max(len(word1),len(word2))):
        if i < len(word1):
            result += word1[i]
        if i < len(word2):
            result += word2[i]
    return result






# ============================================================
# Tests: 把上面的示例改成 assert
# ============================================================

if __name__ == "__main__":
    assert merge_alternately("abc", "pqr") == "apbqcr", "Test 1 failed"
    assert merge_alternately("ab", "pqrs") == "apbqrs", "Test 2 failed"
    assert merge_alternately("abcd", "pq") == "apbqcd", "Test 3 failed"
    print("✅ All tests passed!")
