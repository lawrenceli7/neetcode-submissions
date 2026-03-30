class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= rows or c >= cols
            or (r, c) in visit or grid[r][c] == "0"):
                return

            visit.add((r, c))
            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for dr, dc in directions:
                row, col = dr + r, dc + c
                dfs(row, col)
        
        for r in range(rows):
            for c in range(cols):
                if (grid[r][c] == "1" and (r, c) not in visit):
                    dfs(r, c)
                    islands += 1
        return islands