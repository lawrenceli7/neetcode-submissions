class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(i, combo):
            if len(combo) == k:
                res.append(combo.copy())

            for i in range(i, n + 1):
                combo.append(i)
                backtrack(i + 1, combo)
                combo.pop()

        backtrack(1, [])
        return res
