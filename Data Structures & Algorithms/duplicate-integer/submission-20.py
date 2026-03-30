class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        visit = set()

        for i in range(len(nums)):
            if nums[i] in visit:
                return True
            visit.add(nums[i])
        return False