class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        wordDict = set(wordDict)

        def backtrack(i, curr):
            if i == len(s):
                res.append(" ".join(curr))

            for j in range(i, len(s)):
                word = s[i: j + 1]
                if word in wordDict:
                    curr.append(word)
                    backtrack(j + 1, curr)
                    curr.pop()
        backtrack(0, [])
        return res