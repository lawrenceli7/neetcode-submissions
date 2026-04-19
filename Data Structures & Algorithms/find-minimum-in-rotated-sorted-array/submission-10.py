class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        min_element = nums[left]

        while left <= right:
            if nums[left] < nums[right]:
                min_element = min(min_element, nums[left])

            middle = (left + right) // 2
            min_element = min(min_element, nums[middle])
            # middle is part of the left sorted portion
            if nums[middle] >= nums[left]:
                left = middle + 1
            else:
                right = middle - 1
        return min_element