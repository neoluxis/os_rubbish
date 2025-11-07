from collections import deque
from typing import List

class Solution:
    """
    LeetCode 200. Number of Islands
    https://leetcode.com/problems/number-of-islands/
    """
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        islands = 0

        def bfs(r: int, c: int) -> None:
            queue = deque([(r, c)])
            visited[r][c] = True
            while queue:
                x, y = queue.popleft()
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny] and grid[nx][ny] == "1":
                        visited[nx][ny] = True
                        queue.append((nx, ny))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and not visited[i][j]:
                    islands += 1
                    bfs(i, j)

        return islands