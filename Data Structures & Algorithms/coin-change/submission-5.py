class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        dp = {0: 0}

        def minCoins(a):
            if a in dp:
                return dp[a]

            minn = float("inf")
            for c in coins:
                diff = a - c
                if diff < 0:
                    break
                minn = min(minn, 1 + minCoins(diff))
            
            dp[a] = minn
            return minn

        res = minCoins(amount)
        if res < float("inf"):
            return res
        else:
            return -1