class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visit = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in visit:
                return [visit[diff], i]
            visit[n] = i
        return []