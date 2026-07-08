class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    visit.add((r, c))
                    q.append((r, c))

        def addCell(r, c):
            if r < 0 or r == rows or c < 0 or c == cols or (r, c) in visit or grid[r][c] == -1:
                return
            visit.add((r, c))
            q.append((r, c))

        dist = 0
        while q:
            for i in range(len(q)):
                row, col = q.popleft()
                grid[row][col] = dist
                directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
                for dr, dc in directions:
                    addCell(dr + row, dc + col)
            dist += 1

        