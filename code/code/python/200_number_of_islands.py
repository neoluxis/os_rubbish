class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        visited = [[False]*cols for _ in range(rows)]

        def dfs(r: int, c: int):
            if r < 0 or r >= rows or c < 0 or c >= cols or visited[r][c] or grid[r][c] == "0":
                return
            visited[r][c] = True
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        islands = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and not visited[i][j]:
                    islands += 1
                    dfs(i, j)
        return islands