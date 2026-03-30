class Solution:
    def climbStairs(self, n: int) -> int:
        # def fib(n):
        #     if n == 1:
        #         return 1
        #     if n == 2:
        #         return 2
        #     return fib(n - 1) + fib(n - 2)
        # return fib(n)

        memo = {}
        def fib(n):
            if n in memo:
                return memo[n]
            if n == 1:
                return 1
            if n == 2:
                return 2
            memo[n] = fib(n - 1) + fib(n - 2)
            return memo[n]
        return fib(n)

