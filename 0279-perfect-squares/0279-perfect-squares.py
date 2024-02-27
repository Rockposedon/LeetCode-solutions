class Solution:
    def numSquares(self, n: int) -> int:
        arr = [0] * (n + 1)
        arr[0] = 0
        arr[1] = 1
        
        for i in range(2, n + 1):
            min_squares = float('inf')
            j = 1
            while j * j <= i:
                remaining = i - j * j
                min_squares = min(min_squares, arr[remaining])
                j += 1
            arr[i] = min_squares + 1
        
        return arr[n]