class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr, left, middle, right):
            leftHalf, rightHalf = arr[left: middle + 1], arr[middle + 1: right + 1]
            i, j, k = left, 0, 0

            while j < len(leftHalf) and k < len(rightHalf):
                if leftHalf[j] <= rightHalf[k]:
                    arr[i] = leftHalf[j]
                    j += 1
                    i += 1
                else:
                    arr[i] = rightHalf[k]
                    k += 1
                    i += 1

            while j < len(leftHalf):
                arr[i] = leftHalf[j]
                j += 1
                i += 1

            while k < len(rightHalf):
                arr[i] = rightHalf[k]
                k += 1
                i += 1

        def mergeSort(arr, left, right):
            middle = (left + right) // 2
            if left == right:
                return

            mergeSort(arr, left, middle)
            mergeSort(arr, middle + 1, right)
            merge(arr, left, middle, right)

        mergeSort(nums, 0, len(nums) - 1)
        return nums