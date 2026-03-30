class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    # create a table for text1 (i), text2 (j), and see which character matches
    # if match, check diagonally, if not check the ones next to it
    # initialize out of bounds to 0's

        # initialize row and col to all 0's
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

        # go through the row and col
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                # if they match
                if text1[i] == text2[j]:
                    # add 1 and go diagonal
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    # find max of the two vals, right and below
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])
        # result going to be in the top left of matrix
        return dp[0][0]


