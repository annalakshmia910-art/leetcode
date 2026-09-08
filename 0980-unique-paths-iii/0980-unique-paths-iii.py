class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        empty = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    empty += 1
                elif grid[i][j] == 1:
                    start = (i, j)
        def dfs(i, j, left):
            if grid[i][j] == 2:
                return 1 if left == 0 else 0
            grid[i][j] = -1
            count = 0
            for x, y in [(1,0), (-1,0), (0,1), (0,-1)]:
                ni, nj = i + x, j + y
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] != -1:
                    count += dfs(ni, nj, left - 1)
            grid[i][j] = 0
            return count
        return dfs(start[0], start[1], empty + 1)