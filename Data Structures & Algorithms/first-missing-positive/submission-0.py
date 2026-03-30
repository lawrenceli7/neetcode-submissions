class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        missing = 1

        for n in nums:
            if n > 0 and missing == n:
                missing += 1
        return missing