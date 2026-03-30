class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        currMin = currMax = 1

        for n in nums:
            temp = n * currMax
            currMax = max(n * currMax, n * currMin, n)
            currMin = min(temp, n * currMin, n)
            res = max(res, currMax, currMin)
        return res

