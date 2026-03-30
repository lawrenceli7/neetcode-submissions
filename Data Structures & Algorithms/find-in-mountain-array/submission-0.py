class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        length = mountainArr.length()

        # find peak element
        left, right = 1, length - 2
        while left <= right:
            middle = (left + right) // 2
            l, mid, r = mountainArr.get(middle - 1), mountainArr.get(middle), mountainArr.get(middle + 1)
            if l < mid < r:
                left = middle + 1
            elif l > mid > r:
                right = middle - 1
            else:
                break
        peak = middle

        # search left portion
        left, right = 0, peak
        while left <= right:
            middle = (left + right) // 2
            val = mountainArr.get(middle)
            if val < target:
                left = middle + 1
            elif val > target:
                right = middle - 1
            else:
                return middle

        # search right portion
        left, right = peak, length - 1
        while left <= right:
            middle = (left + right) // 2
            val = mountainArr.get(middle)
            if val > target:
                left = middle + 1
            elif val < target:
                right = middle - 1
            else:
                return middle
        return -1


        