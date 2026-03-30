class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        path = set()

        def dfs(i, r, c):
            # we found the word
            if i == len(word):
                return True
            # out of bounds/invalid cases
            if (r < 0 or c < 0 or
             r >= rows or c >= cols or 
             word[i] != board[r][c] or
             (r, c) in path):
                return False

            # add path
            path.add((r, c))
            # check all 4 directions
            res = (dfs(i + 1, r + 1, c) or
                    dfs(i + 1, r - 1, c) or
                    dfs(i + 1, r, c + 1) or
                    dfs(i + 1, r, c - 1))
            # remove path
            path.remove((r, c))
            return res

        for r in range(rows):
            for c in range(cols):
                if dfs(0, r, c):
                    return True
        return False
