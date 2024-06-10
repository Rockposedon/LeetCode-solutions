class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
        # Create a sorted copy of the input list, hs->(sorted heights)
        hs = sorted(heights)
        
        # If the input list is already sorted
        if heights == hs:
            return 0
        
        # Initialize a counter to keep track of the number of students that need to be moved
        count = 0
        
        # Iterate through the input list and the sorted list simultaneously
        for i in range(len(heights)):
            
            # If the current student in the input list is not in the correct position
            if heights[i]!= hs[i]:
                
                # Increment the counter
                count += 1
        
        # Return the total number of students that need to be moved
        return count