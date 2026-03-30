class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])
        copy = [[matrix[r][c] for c in range(cols)] for r in range(rows)]

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    for col in range(cols):
                        copy[r][col] = 0
                    for row in range(rows):
                        copy[row][c] = 0

        for r in range(rows):
            for c in range(cols):
                matrix[r][c] = copy[r][c]

        