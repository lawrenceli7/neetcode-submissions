class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # only add open parenthesis if open < n
        # only add close parenthesis if close < open
        # valid if open == close == n
        
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