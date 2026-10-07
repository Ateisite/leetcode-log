"""
LeetCode #1275 - Find Winner on a Tic Tac Toe Game
Difficulty: Easy
Topics: Array, Matrix, Hash Table
Date: 2026-10-07
Time spent: 40 min
Status: Solved

## Problem Statement
Tic-tac-toe is played by two players A and B on a 3 x 3 grid.

- Player A always places 'X', player B always places 'O'.
- Players take turns placing characters into empty squares.
- The game ends when there are three of the same character filling any
  row, column, or diagonal.
- The game also ends if all squares are non-empty.

Given moves[i] = [rowi, coli], return:
- "A" if A wins
- "B" if B wins
- "Draw" if game ends in a draw
- "Pending" if there are still moves to play

## Idea
Simulate a 3x3 grid. Player A places 1, player B places -1. Use enumerate
to track turns. Check all rows and columns in a loop, then check the two
diagonals. If any sum equals 3, A wins; if -3, B wins. After all checks,
return "Pending" if moves < 9, otherwise "Draw".

## Complexity
- Time: O(n) where n = len(moves) for placing + O(1) for checking 8 lines
- Space: O(1) for the fixed 3x3 grid

## Submission Log
- [x] Submitted on LeetCode
- [x] Passed all test cases
"""


# ============================================================
# LeetCode Submission (copy entire block to LeetCode)
# ============================================================

class Solution(object):
    def tictactoe(self, moves):
      grid = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]

      for i, (row, col) in enumerate(moves):
          if i % 2 == 0:          # A 的回合
              grid[row][col] = 1
          else:                   # B 的回合
              grid[row][col] = -1
      #计算行，列
      for i in range(3):
          row_sum = grid[i][0] + grid[i][1] + grid[i][2]
          col_sum = grid[0][i] + grid[1][i] + grid[2][i]
          if row_sum == 3 or col_sum == 3:
              return "A"
          if row_sum == -3 or col_sum == -3:
              return "B"

      #计算对角线    
      x = grid[0][0] + grid[1][1] + grid[2][2]
      y = grid[0][2] + grid[1][1] + grid[2][0]

      for v in [ x, y]:
        if abs(v) == 3:
          return "A" if v == 3 else "B"

      if len(moves) < 9:
         return "Pending"
      return "Draw"
         
   
