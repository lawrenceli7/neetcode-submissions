class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # nums.sort()
        # n = len(nums)
        # for i in range(n):
        #     if nums[i] != i:
        #         return i
        # return n

        # numSet = set(nums)
        # n = len(nums)
        # for i in range(n + 1):
        #     if i not in numSet:
        #         return i

        # n = len(nums)
        # xorr = n
        # for i in range(n):
        #     xorr ^= i ^ nums[i]
        # return xorr

        res = len(nums)

        for i in range(len(nums)):
            res += (i - nums[i])
        return res