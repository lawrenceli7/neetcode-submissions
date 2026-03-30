class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtracking(openP, closeP, combo):
            if openP == closeP == n:
                res.append("".join(combo))
                return

            if openP < n:
                combo.append("(")
                backtracking(openP + 1, closeP, combo)
                combo.pop()

            if closeP < openP:
                combo.append(")")
                backtracking(openP, closeP + 1, combo)
                combo.pop()
        backtracking(0, 0, [])
        return res
