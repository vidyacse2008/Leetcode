"""
Day 5 - LeetCode 994: Rotting Oranges (Medium)

You are given an m x n grid where each cell is:
    0 = empty,   1 = a fresh orange,   2 = a rotten orange.
Every minute, each fresh orange that is 4-directionally adjacent (up, down, left,
right) to a rotten orange becomes rotten.

Return the MINIMUM number of minutes until no fresh orange is left. If that is
impossible, return -1.

Example 1:  grid = [[2,1,1],[1,1,0],[0,1,1]]  ->  4
Example 2:  grid = [[2,1,1],[0,1,1],[1,0,1]]  ->  -1
            (the orange in the bottom-left corner is never reached)
Example 3:  grid = [[0,2]]                    ->  0
            (no fresh oranges at minute 0, so the answer is 0)

Constraints:
    1 <= m, n <= 10
    grid[i][j] is 0, 1 or 2   (integers)

The guide's pattern ("multi-source BFS"): ALL rotten oranges spread at the same
time, so start the queue with every rotten orange at once. BFS visits cells in
order of distance, so process the queue one "level" (= one minute) at a time.
Think about: how do you know at the end whether any fresh orange was missed?

Run your tests with:  pytest test_rottingoranges.py
"""


from collections import deque


class Solution:
    def orangesRotting(self, grid):
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0

        # multi-source BFS: every rotten orange starts spreading at minute 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        minutes = 0
        while queue and fresh > 0:
            minutes += 1                           # one level of the queue = one minute
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                        grid[nx][ny] = 2           # becomes rotten (this changes the input)
                        fresh -= 1
                        queue.append((nx, ny))

        return minutes if fresh == 0 else -1       # leftover fresh oranges were unreachable
