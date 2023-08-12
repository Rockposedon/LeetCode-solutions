class Solution(object):
    def uniquePathsWithObstacles(self, a):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m, n = len(a), len(a[0])
        dp = [0] * n        
        dp[0] = 1
        for i in range(m):            
            for j in range(n):
                if not a[i][j]:                                        
                    if j >= 1 and not a[i][j-1]: dp[j] += dp[j-1] 
                else: dp[j] = 0                    
        return dp[-1]
        