class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        res = 0

        while left <= right:
            middle = (left + right) // 2
            if middle * middle == x:
                return middle
            elif middle * middle < x:
                left = middle + 1
                res = middle
            else:
                right = middle - 1
        return res