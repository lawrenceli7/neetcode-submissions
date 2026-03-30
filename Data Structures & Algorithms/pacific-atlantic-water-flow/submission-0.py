class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # start from the outside and work from the inside
        # start from the oceans and see which nodes can reach the oceans
        # add which nodes reach both the oceans

        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visit, prevHeight):
            if ((r, c) in visit or r < 0 or c < 0 or 
            r == rows or c == cols or heights[r][c] < prevHeight):
                return
            visit.add((r, c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        # go through the rows
        for c in range(cols):
            # first row -> touching the pac
            dfs(0, c, pac, heights[0][c])
            # last row -> touching the atl
            dfs(rows - 1, c, atl, heights[rows - 1][c])

        # go through the cols
        for r in range(rows):
            # first/ leftmost col -> touching the pac
            dfs(r, 0, pac, heights[r][0])
            # last/rightmost col -> touching the atl
            dfs(r, cols - 1, atl, heights[r][cols - 1])

        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res




