class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n, ans = len(matrix), len(matrix[0]), 0
        
        # Cumulative sum along each column
        for j in range(n):
            for i in range(1, m):
                matrix[i][j] += matrix[i-1][j] if matrix[i][j] else 0
                
        # Sort each row in descending order
        for row in matrix:
            row.sort(reverse=True)
            
            # Calculate the area of the largest rectangle in the histogram
            for j, val in enumerate(row):
                ans = max(ans, (j+1) * val)
        
        return ans