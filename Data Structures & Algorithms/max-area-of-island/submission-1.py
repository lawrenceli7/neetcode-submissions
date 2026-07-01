class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        res = 0

        def dfs(r, c):
            if r < 0 or r == rows or c < 0 or c == cols or (r, c) in visit or grid[r][c] == 0:
                return 0

            visit.add((r, c))
            area = 1
            directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
            for dr, dc in directions:
                row, col = dr + r, dc + c
                area += dfs(row, col)
            return area

        for r in range(rows):
            for c in range(cols):
                res = max(res, dfs(r, c))
        return res

        