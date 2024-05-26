from functools import cache

class Solution:
    def fib(self, n: int) -> int:
        # Memoized Fibonacci calculation
        @cache
        def fn(n):
            # Base cases
            if n == 0:
                return 0
            if n == 1:
                return 1
            # Recursive calculation
            return fn(n-1) + fn(n-2)
        
        return fn(n)
