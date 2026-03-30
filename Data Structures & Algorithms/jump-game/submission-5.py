class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        def canReach(i):
            if i == len(nums) - 1:
                return True
            
            for jump in range(1, nums[i] + 1):
                if canReach(i + jump):
                    return True
            return False

        return canReach(0)