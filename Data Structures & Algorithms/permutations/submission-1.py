class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtracking(perm):
            if len(nums) == len(perm):
                res.append(perm.copy())
                return

            for n in nums:
                if n not in perm:
                    perm.append(n)
                    backtracking(perm)
                    perm.pop()
        backtracking([])
        return res