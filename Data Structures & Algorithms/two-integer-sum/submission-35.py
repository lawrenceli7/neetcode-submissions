class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valToIdx = {} 

        for i, n in enumerate(nums):
            diff = target - n

            if diff in valToIdx:
                return [valToIdx[diff], i]
            
            valToIdx[n] = i
        return []