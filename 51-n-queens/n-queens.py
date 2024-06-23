class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def b(a):
            if a == n:
                ans.append(["".join(a) for a in c])
                return
            for i in range(n):
                if not e[i] and not d[a+i] and not rev[a-i]:
                    c[a][i] = 'Q'
                    e[i], d[a+i], rev[a-i] = True, True, True
                    b(a+1)
                    c[a][i] = '.'
                    e[i], d[a+i], rev[a-i] = False, False, False
        
        c= [['.' for j in range(n)] for j in range(n)]
        e, d, rev = [False]*n, [False]*(2*n), [False]*(2*n-1)
        ans = []
        b(0)
        return ans