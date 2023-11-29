class Solution:
    def hammingWeight(self, n: int) -> int:
        # Initialize a counter variable to 0
        count = 0
        # Loop until n is 0
        while n != 0:
            # If the last bit of n is 1, increment the counter
            if n & 1 == 1:
                count += 1
            # Shift n to the right by 1 bit
            n = n >> 1
        # Return the counter
        return count