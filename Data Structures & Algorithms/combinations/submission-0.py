class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtracking(start, combo):
            if len(combo) == k:
                res.append(combo.copy())
                return

            for i in range(start, n + 1):
                combo.append(i)
                backtracking(i + 1, combo)
                combo.pop()

        backtracking(1, [])
        return res
