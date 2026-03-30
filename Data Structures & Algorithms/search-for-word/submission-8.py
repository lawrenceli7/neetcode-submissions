class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visit = set()

        def backtrack(i, r, c):
            if i == len(word):
                return True

            if r < 0 or c < 0 or r == rows or c == cols or (r, c) in visit or board[r][c] != word[i]:
                return False
            
            visit.add((r, c))
            directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
            for dr, dc in directions:
                row, col = dr + r, dc + c
                if backtrack(i + 1, row, col):
                    return True
            visit.remove((r, c))
            return False

        for r in range(rows):
            for c in range(cols):
                if backtrack(0, r, c):
                    return True
        return False