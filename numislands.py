"""
Day 5 - LeetCode 200: Number of Islands (Medium)

Given an m x n grid of '1' (land) and '0' (water), return the number of islands.
An island is a group of '1's connected horizontally or vertically (NOT
diagonally). You may assume all four edges of the grid are surrounded by water.

Example 1:
    grid = [["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]]          ->  1

Example 2:
    grid = [["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]]          ->  3

Constraints:
    1 <= m, n <= 300
    grid[i][j] is '0' or '1'      (strings, not integers!)

The guide's pattern ("grid DFS"): every cell is a node, its neighbours are up,
down, left and right. Walk the grid; whenever you meet unvisited land, count one
island and "sink" or mark the whole island so it is never counted again. Always
check the bounds before looking at a neighbour.

Watch out: a 300 x 300 grid of all land is a single island with 90,000 cells.
A recursive DFS that deep raises RecursionError in Python. Use BFS with a deque
(from collections import deque), or an explicit stack, or raise the recursion
limit.

Run your tests with:  pytest test_numislands.py
"""


from collections import deque


class Solution:
    def numIslands(self, grid):
        rows, cols = len(grid), len(grid[0])
        count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != "1":
                    continue
                # found unvisited land: one more island, so sink all of it with BFS
                count += 1
                grid[r][c] = "0"                   # mark visited (this changes the input)
                queue = deque([(r, c)])
                while queue:
                    x, y = queue.popleft()
                    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == "1":
                            grid[nx][ny] = "0"     # mark when queued, so it is queued only once
                            queue.append((nx, ny))
        return count
