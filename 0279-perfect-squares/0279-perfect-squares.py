class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        
        for i in range(2, n + 1):
            min_squares = float('inf')
            j = 1
            while j * j <= i:
                remaining = i - j * j
                min_squares = min(min_squares, dp[remaining])
                j += 1
            dp[i] = min_squares + 1
        
        return dp[n]