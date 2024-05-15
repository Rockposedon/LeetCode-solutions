class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        
        # Variable to store the maximum value found in the matrix(mat)
        max_value = 0  
        
        # List to store positions(index) of the all peaks in mat
        peak_positions = []  
        
        # Number of rows in the matrix
        num_rows = len(mat)  
        
        # Iterate through each row in the matrix
        for i in range(num_rows):
            
            # Iterate through each column in the current row
            for j in range(len(mat[0])): 
                
                # If the current cell's value is greater than the current maximum value, then update max_val
                if mat[i][j] > max_value:
                    max_value = mat[i][j]  
                    
                    # Add the position(index) of the peak to the list
                    peak_positions.append([i, j])  
                    
        # Return the position of the last peak found
        return peak_positions[-1]  