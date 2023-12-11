class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        
        # Calculate the size of the subarray that needs to contain the special integer
        size = len(arr) // 4

        # Iterate through the array
        for i in range(len(arr) - size):
            
            # Check if the current element is equal to the element size positions ahead
            if arr[i] == arr[i + size]:
                
                # If true, the current element is the special integer
                return arr[i]
        
        # If no special integer is found, return -1
        return -1