class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        memo = {0: 0}

        def minCoins(a):
            if a in memo:
                return memo[a]
            
            res = float("inf")
            for c in coins:
                diff = a - c
                if diff < 0:
                    break
                res = min(res, 1 + minCoins(diff))
            memo[a] = res
            return res

        res = minCoins(amount)
        if res < float("inf"):
            return res
        else:
            return -1