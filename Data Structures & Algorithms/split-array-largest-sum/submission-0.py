class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left, right = max(nums), sum(nums)
        res = sum(nums)

        def canSplit(largest):
            subarray = 0
            currSum = 0

            for n in nums:
                currSum += n
                if currSum > largest:
                    subarray += 1
                    currSum = n
            return subarray + 1 <= k

        while left <= right:
            middle = (left + right) // 2

            if canSplit(middle):
                res = middle
                right = middle - 1
            else:
                left = middle + 1
        return res