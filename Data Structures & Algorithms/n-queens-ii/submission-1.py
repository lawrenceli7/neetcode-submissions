class Solution:
    def totalNQueens(self, n: int) -> int:
        posDiag = set()
        negDiag = set()
        col = set()
        res = 0

        def backtracking(r):
            nonlocal res
            if r == n:
                res += 1
                return

            for c in range(n):
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue

                col.add(c)
                posDiag.add((r + c))
                negDiag.add((r - c))
                backtracking(r + 1)
                col.remove(c)
                posDiag.remove((r + c))
                negDiag.remove((r - c))
        backtracking(0)
        return res
