class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        nRows, nCols = len(grid), len(grid[0])  # Get the number of rows and columns in the grid
        visited = set()  # A set to keep track of visited cells

        # Function to check if a cell is within grid boundaries
        def inBound(row, col):
            return 0 <= row < nRows and 0 <= col < nCols

        # Depth-First Search (DFS) function to explore all possible paths from a cell
        def dfs(row, col):
            # If the cell is out of bounds, already visited, or has zero gold, return 0
            if not inBound(row, col) or (row, col) in visited or grid[row][col] == 0:
                return 0

            visited.add((row, col))  # Mark the cell as visited

            # Explore all four possible directions (left, right, up, down)
            left = dfs(row, col - 1)
            right = dfs(row, col + 1)
            up = dfs(row - 1, col)
            down = dfs(row + 1, col)

            visited.remove((row, col))  # Unmark the cell to allow for other paths

            # Return the current cell's gold plus the maximum gold from any direction
            return grid[row][col] + max(left, right, up, down)

        maxGold = 0  # Initialize the maximum gold to 0

        # Iterate over each cell in the grid
        for row in range(nRows):
            for col in range(nCols):
                # If the cell has gold and is not visited, perform DFS to find the maximum gold path
                if grid[row][col] and (row, col) not in visited:
                    maxGold = max(maxGold, dfs(row, col))  # Update maxGold with the highest value found

        return maxGold  # Return the maximum gold collected
