class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2

        # ensure A is the smaller array
        if len(A) > len(B):
            A, B = B, A

        # binary search on partition positions: 0..len(A)
        left, right = 0, len(A)
        while left <= right:
            # middle is the number of elements in A's left partition
            middle = (left + right) // 2
            j = half - middle  # number of elements in B's left partition

            # boundary values (use -inf / +inf for empty partitions)
            Aleft = A[middle - 1] if middle - 1 >= 0 else float("-inf")
            Aright = A[middle] if middle < len(A) else float("inf")
            Bleft = B[j - 1] if j - 1 >= 0 else float("-inf")
            Bright = B[j] if j < len(B) else float("inf")

            # found correct partition
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:  # odd
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2.0
            # move partition in A left or right
            elif Aleft > Bright:
                right = middle - 1
            else:
                left = middle + 1

        # should never reach here for valid inputs
        return 0.0
