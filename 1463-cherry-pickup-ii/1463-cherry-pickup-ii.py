class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        R,C = len(grid)-1,len(grid[0])-1
        dir = (-1,0,1)

        @cache
        def dp(r1,c1,c2):
            k = 0
            if c1 == c2:
                k = grid[r1][c1]
            else:
                k = grid[r1][c1] + grid[r1][c2]

            if r1 == R:
                return k
            
            ans = 0
            for a in dir:
                for b in dir:
                    if 0<=a+c1<=C and 0<=b+c2<=C:
                        ans = max(ans,dp(r1+1,a+c1,b+c2))
            return ans+k

        return dp(0,0,C)
                        