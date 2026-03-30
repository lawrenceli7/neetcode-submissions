class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        top, bottom = 0, rows - 1

        while top <= bottom:
            middleRow = (top + bottom) // 2
            if target > matrix[middleRow][-1]:
                top = middleRow + 1
            elif target < matrix[middleRow][0]:
                bottom = middleRow - 1
            else:
                break

        targetRow = (top + bottom) // 2
        left, right = 0, cols - 1

        while left <= right:
            middle = (left + right) // 2
            if target > matrix[targetRow][middle]:
                left = middle + 1
            elif target < matrix[targetRow][middle]:
                right = middle - 1
            else:
                return True
        return False