class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def backtracking(i, total):
            if i == len(nums):
                return total
            
            return backtracking(i + 1, total ^ nums[i]) + backtracking(i + 1, total)
        return backtracking(0, 0)