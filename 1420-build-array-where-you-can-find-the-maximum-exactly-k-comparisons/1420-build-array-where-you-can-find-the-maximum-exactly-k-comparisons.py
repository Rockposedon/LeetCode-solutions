class Solution:
    def numOfArrays(self, n, m, k):
        mod = 10**9 + 7
        memo = {}

        def dp(n, k, curmax):
            if n == 0:
                return int(k == 0)
            if k < 0:
                return 0
            if (n, k, curmax) in memo:
                return memo[(n, k, curmax)]

            ways = 0
            for pick in range(1, m + 1):
                cost = int(pick > curmax)
                ways += dp(n - 1, k - cost, max(pick, curmax))
                ways %= mod

            memo[(n, k, curmax)] = ways
            return ways

        return dp(n, k, 0)