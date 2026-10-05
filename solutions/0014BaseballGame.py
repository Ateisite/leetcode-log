"""
LeetCode #682 - Baseball Game
Difficulty: Easy
Topics: Array, Stack
Date: 2026-10-05
Time spent: 35 min
Status: Solved

## Problem Statement
You are keeping the scores for a baseball game with strange rules. At the
beginning of the game, you start with an empty record.

You are given a list of strings operations, where operations[i] is the ith
operation you must apply to the record and is one of the following:

- An integer x: Record a new score of x.
- "+": Record a new score that is the sum of the previous two scores.
- "D": Record a new score that is the double of the previous score.
- "C": Invalidate the previous score, removing it from the record.

Return the sum of all the scores on the record after applying all the
operations.

Example 1:
Input: ops = ["5","2","C","D","+"]
Output: 30
"5" - record [5]
"2" - record [5, 2]
"C" - record [5]
"D" - record [5, 10]
"+" - record [5, 10, 15]
Sum = 30

Example 2:
Input: ops = ["5","-2","4","C","D","9","+","+"]
Output: 27

Example 3:
Input: ops = ["1","C"]
Output: 0

## Idea
Use a list record to track all valid scores. Iterate through operations:
- "+" → append sum of last two scores in record
- "D" → append double of the last score
- "C" → pop (remove) the last score
- integer string → append int(value) to record
Finally return sum(record).

## Complexity
- Time: O(n) single pass through operations
- Space: O(n) for the record list

## Submission Log
- [x] Submitted on LeetCode
- [x] Passed all test cases
"""


# ============================================================
# LeetCode Submission (copy entire block to LeetCode)
# ============================================================

class Solution(object):
    def calPoints(self, operations):
        record = []
        for i in range(len(operations)):
            if operations[i] == "+":
                record.append(record[-1] + record[-2])
            elif operations[i] == "D":
                record.append(record[-1]*2)
            elif operations[i] == "C":
                record.pop()
            else:
                record.append(int(operations[i]))
        return sum(record)
