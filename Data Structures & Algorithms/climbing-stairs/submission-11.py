class Solution:
    def climbStairs(self, n: int) -> int:
        # def fib(n):
        #     if n == 1:
        #         return 1
        #     if n == 2:
        #         return 2
        #     return fib(n - 1) + fib(n - 2)
        # return fib(n)

        # memo = {}
        # def fib(n):
        #     if n in memo:
        #         return memo[n]
        #     if n == 1:
        #         return 1
        #     if n == 2:
        #         return 2
        #     memo[n] = fib(n - 1) + fib(n - 2)
        #     return memo[n]
        # return fib(n)

        if n == 1:
            return 1
        if n == 2:
            return 2
        dp = [0] * n
        dp[0] = 1
        dp[1] = 2

        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n - 1]


