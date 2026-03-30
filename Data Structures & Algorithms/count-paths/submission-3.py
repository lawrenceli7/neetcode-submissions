class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def helper(i, j):
            if i == 0 and j == 0:
                return 1
            elif i < 0 or j < 0 or i >= m or j >= n:
                return 0
            else:
                return helper(i, j - 1) + helper(i - 1, j)
        return helper(m - 1, n - 1)