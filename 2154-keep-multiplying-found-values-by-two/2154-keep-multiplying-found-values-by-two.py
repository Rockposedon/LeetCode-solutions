class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        
        # Loop until the original value is not found in the list
        while original in nums:
            
            # Multiply the original value by 2
            original *= 2
            
        # Return the final value of original
        return original