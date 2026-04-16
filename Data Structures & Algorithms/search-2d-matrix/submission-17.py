class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])       
        top, bottom = 0, rows - 1
        
        while top <= bottom:
            middleRow = (top + bottom) // 2
            if matrix[middleRow][-1] < target:
                top = middleRow + 1
            elif matrix[middleRow][0] > target:
                bottom = middleRow - 1
            else:
                break

        targetRow = (top + bottom) // 2
        left, right = 0, cols - 1

        while left <= right:
            middle = (left + right) // 2
            if matrix[targetRow][middle] < target:
                left = middle + 1
            elif matrix[targetRow][middle] > target:
                right = middle - 1
            else:
                return True
        return False