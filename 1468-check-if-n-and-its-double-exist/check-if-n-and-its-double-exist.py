class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        # Create a set to store the numbers we have seen so far
        seen = set()
        
        # Iterate through each number in the array
        for num in arr:
            
            # Check if the double of the current number is already in the set
            # or if the current number is even and half of it is in the set
            if num * 2 in seen or (num % 2 == 0 and num // 2 in seen):
                return True
            
            # Add the current number to the set
            seen.add(num)
        
        # If no such pair is found, return False
        return False