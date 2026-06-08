class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = []

        digits_to_char = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz",
        }

        def backtrack(i, currStr):
            if len(digits) == len(currStr):
                res.append(currStr)
                return

            for char in digits_to_char[digits[i]]:
                backtrack(i + 1, currStr + char)

        backtrack(0, "")
        return res