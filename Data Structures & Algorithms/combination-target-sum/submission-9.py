class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtracking(i, total, combo):
            if total == target:
                res.append(combo.copy())
                return

            if total > target or i == len(nums):
                return

            combo.append(nums[i])
            backtracking(i, total + nums[i], combo)
            combo.pop()

            backtracking(i + 1, total, combo)
        backtracking(0, 0, [])
        return res