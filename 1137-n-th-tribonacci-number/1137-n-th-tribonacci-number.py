class Solution:
    def tribonacci(self, n: int) -> int:
        @cache
        def ts(n):
            if n == 0 :
                return 0
            elif n <= 2:
                return 1
            
            return ts(n-1)+ts(n-3)+ts(n-2)
        return ts(n)
    
