class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def backtracking(i, part):
            if i == len(s):
                res.append(part.copy())
                return
            for j in range(i, len(s)):
                if self.isPali(s, i, j):
                    part.append(s[i: j + 1])
                    backtracking(j + 1, part)
                    part.pop()
        backtracking(0, [])
        return res


    def isPali(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
            