class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        res = nums[0]
        
        while left <= right:
            if nums[left] < nums[right]:
                res = min(res, nums[left])

            middle = (left + right) // 2
            res = min(res, nums[middle])

            if nums[middle] >= nums[left]:
                left = middle + 1
            else:
                right = middle - 1
        return res
