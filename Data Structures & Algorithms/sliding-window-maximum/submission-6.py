class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []

        for i in range(len(nums) - k + 1):
            maxNum = nums[i]
            for j in range(i + 1, i + k):
                maxNum = max(maxNum, nums[j])
            res.append(maxNum)
        return res