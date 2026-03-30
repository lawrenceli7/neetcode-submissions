class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        wordDict = set(wordDict)

        def backtracking(i, curr):
            if i == len(s):
                res.append(" ".join(curr))
                return

            for j in range(i, len(s)):
                w = s[i: j + 1]
                if w in wordDict:
                    curr.append(w)
                    backtracking(j + 1, curr)
                    curr.pop()
        backtracking(0, [])
        return res

