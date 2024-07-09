class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        # Create a list of friends numbered from 1 to n
        friend = list(range(1, n + 1))  
        # Initialize starting index
        idx = 0  
        
        # Continue until only one friend is left
        while len(friend) > 1:  
            
            # Calculate the index of the friend to remove
            idx = (idx + k - 1) % len(friend) 
            # Remove the friend at the calculated index
            friend.pop(idx) 
        
        # Return the last remaining friend
        return friend[0]  
