class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        # Get the dimensions of the grid
        m = len(grid)
        n = len(grid[0])

        # Initialize the difference matrix
        diff = [[0 for _ in range(n)] for _ in range(m)]

        # Calculate differences along rows
        for i in range(m):
            row_difference = 0
            for j in range(n):
                # Count ones as +1 and zeros as -1
                if grid[i][j] == 1:
                    row_difference += 1
                else:
                    row_difference -= 1
            # Update the differences matrix for the row
            for j in range(n):
                diff[i][j] += row_difference

        # Calculate differences along columns
        for j in range(n):
            col_difference = 0
            for i in range(m):
                # Count ones as +1 and zeros as -1
                if grid[i][j] == 1:
                    col_difference += 1
                else:
                    col_difference -= 1
            # Update the differences matrix for the column
            for i in range(m):
                diff[i][j] += col_difference

        # Return the differences matrix
        return diff