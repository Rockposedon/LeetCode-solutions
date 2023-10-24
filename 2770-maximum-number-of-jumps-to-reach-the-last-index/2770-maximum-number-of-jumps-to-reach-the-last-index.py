class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        # Get the length of the input array
        n = len(nums)
        
        # Initialize a dynamic programming array to store maximum jumps for each index.
        dp = [-1] * n
        
        # Starting from index 0, set the initial jump count to 0
        dp[0] = 0
        
        # Iterate through the array starting from index 1
        for i in range(1, n):
            # For each index i, iterate through previous indices (j)
            for j in range(i):
                # Check if it's possible to jump from index j to index i
                if dp[j] >= 0 and abs(nums[i] - nums[j]) <= target:
                    # If a valid jump is possible, update dp[i] with the maximum of its current value and dp[j] + 1
                    dp[i] = max(dp[i], dp[j] + 1)
        
        # Return the maximum jumps needed to reach the last index (dp[-1])
        return dp[-1]
