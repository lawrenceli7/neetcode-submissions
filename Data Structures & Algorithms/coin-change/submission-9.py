class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        dp = [0] * (amount + 1)

        for i in range(1, amount + 1):
            res = float("inf")
            for c in coins:
                diff = i - c
                if diff < 0:
                    break

                res = min(res, 1 + dp[diff])
            dp[i] = res

        if dp[amount] < float("inf"):
            return dp[amount]
        else:
            return -1