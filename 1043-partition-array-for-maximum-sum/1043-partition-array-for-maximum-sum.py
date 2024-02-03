class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        # Create an array to store the maximum sum for each position in the original array.
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            maxVal = 0  # Initialize maxVal to 0 for each position i in the original array.
            
            for j in range(1, min(k, i) + 1): 

                # Update maxVal with the maximum value in the current subarray of length at most k.
                maxVal = max(maxVal, arr[i - j]) 

                # Update the maximum sum at position i by considering the current subarray.
                dp[i] = max(dp[i], dp[i - j] + maxVal * j)

        return dp[n]  # Return the maximum sum after partitioning the entire array.