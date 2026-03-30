class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def quickSelect(left, right):
            less = left
            greater = right
            pivot = nums[right]
            equal = left

            while equal <= greater:
                while equal <= greater and nums[equal] < pivot:
                    nums[equal], nums[less] = nums[less], nums[equal]
                    less += 1
                    equal += 1
                while equal <= greater and nums[equal] > pivot:
                    nums[equal], nums[greater] = nums[greater], nums[equal]
                    greater -= 1
                while equal <= greater and nums[equal] == pivot:
                    equal += 1

            if k > greater:
                return quickSelect(greater + 1, right)
            elif k < less:
                return quickSelect(left, less - 1)
            else:
                return nums[less] or nums[greater]
        return quickSelect(0, len(nums) - 1)
        
