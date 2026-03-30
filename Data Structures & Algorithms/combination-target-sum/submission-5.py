class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, total, curr):
            if total == target:
                res.append(curr.copy())
                return
            if total > target or i < 0 or i >= len(nums):
                return

            curr.append(nums[i])
            dfs(i, total + nums[i], curr)
            curr.remove(nums[i])

            dfs(i + 1, total, curr)

        dfs(0, 0, [])
        return res