"""
LeetCode #1232 - Check If It Is a Straight Line
Difficulty: Easy
Topics: Array, Math, Geometry
Date: 2026-10-17
Time spent: 25 min
Status: Solved

## Problem Statement
Given coordinates[i] = [x, y], check if all points lie on a straight line.

Example 1:
Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true

Example 2:
Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false

## Idea
Use first two points as baseline. For each subsequent point, check if
it lies on the same line using cross-multiplication to avoid division:
(y1-y0)*(x-x0) == (y-y0)*(x1-x0). If any point fails, return False.

## Complexity
- Time: O(n) — single pass through coordinates
- Space: O(1)

## Submission Log
- [x] Submitted on LeetCode
- [x] Passed all test cases
"""


# ============================================================
# LeetCode Submission (copy entire block to LeetCode)
# ============================================================

class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]

        for i in range(2, len(coordinates)):
            x, y = coordinates[i]
            if (y1 - y0) * (x - x0) != (y - y0) * (x1 - x0):
                return False
        return True


