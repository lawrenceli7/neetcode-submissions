class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        currSum = 0
        res = 0
        prefixSum = defaultdict(int)
        prefixSum[0] = 1

        for n in nums:
            currSum += n
            diff = currSum - k
            res += prefixSum[diff]
            prefixSum[currSum] += 1
        return res