class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        atl, pac = set(), set()
        rows, cols = len(heights), len(heights[0])

        def dfs(r, c, prev, visit):
            if (r < 0 or c < 0 or r >= rows or
            c >= cols or (r, c) in visit or 
            heights[r][c] < prev):
                return

            visit.add((r, c))
            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for dr, dc in directions:
                row, col = dr + r, dc + c
                dfs(row, col, heights[r][c], visit)

        for c in range(cols):
            dfs(0, c, heights[0][c], pac)
            dfs(rows - 1, c, heights[rows - 1][c], atl)

        for r in range(rows):
            dfs(r, 0, heights[r][0], pac)
            dfs(r, cols - 1, heights[r][cols - 1], atl)

        res = []
        for r in range(rows):
            for c in range (cols):
                if (r, c) in atl and (r, c) in pac:
                    res.append([r, c])
        return res
