class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        # Initialize variables
        ans = 0  # Counter for minimum operations
        k = 0    # Position of the current bit
        mask = 1 # Bit mask to check each bit of n
        
        # Iterate through each bit of n
        while mask <= n:
            # Check if the current bit is set in n
            if n & mask:
                # If set, perform the bitwise operation to update ans
                ans = 2 ** (k + 1) - 1 - ans
                
            # Move the bit mask to the next position
            mask <<= 1
            # Increment the position counter
            k += 1
        
        # Return the minimum number of one-bit operations
        return ans
