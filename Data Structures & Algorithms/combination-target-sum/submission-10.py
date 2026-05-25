class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, total, combo):
            if total == target:
                res.append(combo.copy())
                return
            
            if total > target or i == len(nums):
                return

            combo.append(nums[i])
            backtrack(i, total + nums[i], combo)
            combo.pop()

            backtrack(i + 1, total, combo)
        backtrack(0, 0, [])
        return res