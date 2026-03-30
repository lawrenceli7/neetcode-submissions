class Solution:
    def countBits(self, n: int) -> List[int]:
        # mod by 2, then shift bits to the right by / 2
        # offset/significant bits [1, 2, 4, 8, 16]
        # n
        # 0 - 0000 -> 0
        # 1 - 0001 -> 1 + dp[n - 1]
        # 2 - 0010 -> 1 + dp[n - 2]
        # 3 - 0011 -> 1 + dp[n - 2]
        # 4 - 0100 -> 1 + dp[n - 4]
        # 5 - 0101 -> 1 + dp[n - 4]
        # 6 - 0110 -> 1 + dp[n - 4] -> 2
        # 7 - 0111 -> 3
        # 8 - 1000 -> 1 + dp[n - 8]

        dp = [0] * (n + 1)
        offset = 1

        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        return dp
