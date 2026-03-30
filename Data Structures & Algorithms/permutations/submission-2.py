class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(perm):
            if len(perm) == len(nums):
                res.append(perm.copy())
            
            for n in nums:
                if n not in perm:
                    perm.append(n)
                    backtrack(perm)
                    perm.pop()
        backtrack([])
        return res