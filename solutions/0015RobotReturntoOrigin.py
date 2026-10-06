"""
LeetCode #657 - Robot Return to Origin
Difficulty: Easy
Topics: String, Simulation
Date: 2026-10-06
Time spent: 15 min
Status: Solved

## Problem Statement
There is a robot starting at the position (0, 0), the origin, on a 2D plane.
Given a sequence of its moves, judge if this robot ends up at (0, 0) after
it completes its moves.

Valid moves are 'R' (right), 'L' (left), 'U' (up), and 'D' (down).

Return true if the robot returns to the origin after it finishes all of its
moves, or false otherwise.

Example 1:
Input: moves = "UD"
Output: true

Example 2:
Input: moves = "LL"
Output: false

## Idea
Simulate the robot's movement. Use x and y coordinates starting at (0, 0).
For each move: U increments y, D decrements y, L decrements x, R increments x.
After processing all moves, return True if both x and y are 0.

## Complexity
- Time: O(n) single pass through the moves string
- Space: O(1) only two integer variables

## Submission Log
- [x] Submitted on LeetCode
- [x] Passed all test cases
"""


# ============================================================
# LeetCode Submission (copy entire block to LeetCode)
# ============================================================

class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        x, y = 0, 0
        for c in moves:
            if c == 'U':
                y += 1
            elif c == 'D':
                y -= 1
            elif c == 'L':
                x -= 1
            elif c == 'R':
                x += 1
        return x == 0 and y == 0
