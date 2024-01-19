class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])

        # Loop through each element in the matrix
        for row in range(n):
            for col in range(m):

                # for eftmost column
                if row > 0 and col - 1 == -1:
                    matrix[row][col] = min(matrix[row][col] + matrix[row - 1][col], matrix[row][col] + matrix[row - 1][col + 1])

                # for middle columns
                elif row > 0 and 0 <= col - 1 and col + 1 < m:
                    matrix[row][col] = min(matrix[row][col] + matrix[row - 1][col], matrix[row][col] + matrix[row - 1][col + 1], matrix[row][col] + matrix[row - 1][col-1])
                    
                # for rightmost column
                elif row > 0 and col + 1 == m:
                    matrix[row][col] = min(matrix[row][col] + matrix[row - 1][col], matrix[row][col] + matrix[row - 1][col - 1])

        # Return the minimum value in the last row
        return min(matrix[n - 1])
