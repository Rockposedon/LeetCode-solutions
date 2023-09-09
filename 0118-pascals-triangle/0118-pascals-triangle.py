class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        
        # Initialize the Pascal's Triangle with the first row containing a single '1'.
        triangle = [[1]]
        
        # Loop from the second row (index 1) to numRows (exclusive).
        for i in range(1, numRows):
            # Get the previous row in the triangle.
            prev_row = triangle[-1]
            
            # Create a new row with the first element as '1'.
            new_row = [1]
            
            # Calculate the elements in the new row based on the previous row.
            for j in range(1, len(prev_row)):
                new_row.append(prev_row[j-1] + prev_row[j])
            
            # Add the last element '1' to the new row.
            new_row.append(1)
            
            # Append the new row to the triangle.
            triangle.append(new_row)
        
        # Return the completed Pascal's Triangle.
        return triangle
