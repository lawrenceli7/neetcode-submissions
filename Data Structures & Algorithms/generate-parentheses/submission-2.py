class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(openP, closeP, combo):
            if openP == closeP == n:
                res.append("".join(combo))
                return

            if openP < n:
                combo.append("(")
                backtrack(openP + 1, closeP, combo)
                combo.pop()
            
            if closeP < openP:
                combo.append(")")
                backtrack(openP, closeP + 1, combo)
                combo.pop()
        backtrack(0, 0, [])
        return res