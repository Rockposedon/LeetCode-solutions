class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        # Initialize the current winner and a counter
        currentWinner = arr[0]
        count = 0
        
        for i in range(1, len(arr)):
            
            # Check if the current element is greater than the current winner
            if arr[i] > currentWinner:
                
                currentWinner = arr[i]  # Set the current winner to the new element
                
                count = 1  # Reset the consecutive win counter to 1
                
            else:
                
                count += 1  # Increment the consecutive win counter
            
            # Check if the consecutive win counter has reached 'k'
            if count == k:
                
                return currentWinner  # Return the current winner if it has won 'k' times
        
        # If no winner was found after iterating through the array, return the current winner
        return currentWinner
