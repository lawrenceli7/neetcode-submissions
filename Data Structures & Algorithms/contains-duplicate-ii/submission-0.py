class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        visit = set()
        left = 0

        for right in range(len(nums)):
            if right - left > k:
                visit.remove(nums[left])
                left += 1
            if nums[right] in visit:
                return True
            visit.add(nums[right])
        return False