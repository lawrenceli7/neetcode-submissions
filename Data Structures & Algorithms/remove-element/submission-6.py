class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0

        for right in range(len(nums)):
            if nums[right] != val:
                nums[k] = nums[right]
                k += 1
        return k