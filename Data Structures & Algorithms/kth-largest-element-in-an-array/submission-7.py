class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def quickSelect(left, right):
            less = left
            greater = right
            equal = left
            pivot = nums[right]

            while greater >= equal:
                while greater >= equal and nums[equal] < pivot:
                    nums[less], nums[equal] = nums[equal], nums[less]
                    equal += 1
                    less += 1
                while greater >= equal and nums[equal] > pivot:
                    nums[greater], nums[equal] = nums[equal], nums[greater]
                    greater -= 1
                while greater >= equal and nums[equal] == pivot:
                    equal += 1

            if k > greater:
                return quickSelect(greater + 1, right)
            elif k < less:
                return quickSelect(left, less - 1)
            else:
                return nums[less] or nums[greater]
        return quickSelect(0, len(nums) - 1)