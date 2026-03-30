class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        dp = [0] * (amount + 1)

        for i in range(1, amount + 1):
            minn = float("inf")
            
            for c in coins:
                diff = i - c
                if diff < 0:
                    break
                minn = min(minn, 1 + dp[diff])
            dp[i] = minn

        res = dp[amount]
        if res < float("inf"):
            return res
        else:
            return -1