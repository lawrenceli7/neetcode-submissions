class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def helper(i):
            if i in memo:
                return memo[i]
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0], nums[1])

            memo[i] = max(nums[i] + helper(i - 2), helper(i - 1))
            return memo[i]
        return helper(len(nums) - 1)