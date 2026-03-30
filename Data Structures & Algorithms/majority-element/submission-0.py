class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        element = None

        for n in nums:
            if count == 0:
                element = n
            count += 1 if element == n else -1
        return element