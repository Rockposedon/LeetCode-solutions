class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        # Initialize the transposed matrix
        result_matrix = []  

        # Iterate through each column in the original matrix
        for col in range(len(matrix[0])):
            
            # Initialize a temporary row for the transposed matrix
            temp_row = []  

            # Iterate through each row in the original matrix
            for row in range(len(matrix)):
                
                # Transpose the element and add to the temporary row
                temp_row.append(matrix[row][col])  
             
            # Add the transposed row to the result matrix
            result_matrix.append(temp_row)  
        
        # Return the transposed matrix
        return result_matrix  