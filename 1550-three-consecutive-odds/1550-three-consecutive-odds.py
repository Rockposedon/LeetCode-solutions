class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        
        # Variable to count consecutive odd numbers in the array
        odd_count = 0
        
        # Iterate through each element in the array
        for i in arr:
            # Check if the current element is odd
            if i % 2 == 1:
                # Increment the count of consecutive odd numbers
                odd_count += 1
            else:
                # Reset the count if the current element is not odd
                odd_count = 0
            
            # Check if we have found three consecutive odd numbers
            if odd_count == 3:
                return True  # Return True if three consecutive odd numbers are found
        
        # Return False if no three consecutive odd numbers are found
        return False