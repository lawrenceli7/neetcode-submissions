class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
            
        memo = {0: nums[0], 1: max(nums[0], nums[1])}
        def helper(i):
            if i in memo:
                return memo[i]
            memo[i] = max(nums[i] + helper(i - 2), helper(i - 1))
            return memo[i]
        return helper(len(nums) - 1)