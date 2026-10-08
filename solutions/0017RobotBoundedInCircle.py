"""
LeetCode #1041 - Robot Bounded In Circle
Difficulty: Medium
Topics: Math, Simulation
Date: 2026-10-08
Time spent: 45 min
Status: Solved

## Idea
Simulate the robot's movement once. Use dx, dy arrays to represent the
four directions (N, W, S, E). Track position (x, y) and direction. After
one pass through instructions: if back at origin (0, 0) → bounded (True);
if direction changed (not facing north) → bounded (True); otherwise →
unbounded (False).

## Complexity
- Time: O(n) single pass through instructions
- Space: O(1) only position and direction variables

## Submission Log
- [x] Submitted on LeetCode
- [x] Passed all test cases

## Problem Statement
On an infinite plane, a robot initially stands at (0, 0) facing north.

Instructions:
- "G": go straight 1 unit
- "L": turn 90 degrees left (anti-clockwise)
- "R": turn 90 degrees right (clockwise)

The robot performs the instructions in order, repeats them forever.

Return true if there exists a circle such that the robot never leaves it.

Example 1:
Input: instructions = "GGLLGG"
Output: true

Example 2:
Input: instructions = "GG"
Output: false

Example 3:
Input: instructions = "GL"
Output: true

## Idea
[Write your idea here]

## Complexity
- Time: O(?)
- Space: O(?)

## Submission Log
- [ ] Submitted on LeetCode
- [ ] Passed all test cases
"""


# ============================================================
# LeetCode Submission (copy entire block to LeetCode)
# ============================================================

class Solution(object):
    def isRobotBounded(self, instructions):
        dx = [0, -1, 0, 1] #北西南东
        dy = [1, 0, -1, 0] #北西南东
        direction = 0
        x=0
        y=0
        for c in instructions:
            if c == "G":
                x = x + dx[direction]
                y = y + dy[direction]
            elif c == "L":
                direction = (direction + 1) % 4
            elif c == "R":
                direction = (direction + 3) % 4
        if x == 0 and y == 0:
            return True
        if direction != 0:
            return True
        return False
