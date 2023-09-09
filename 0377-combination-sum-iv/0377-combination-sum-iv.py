class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # Create a list dp to store the number of combinations for each sum
        dp = [0] * (target + 1)
        
        # There's one way to make a sum of 0, which is by not selecting any number
        dp[0] = 1
        
        # Loop through each sum from 1 to the target
        for i in range(1, target + 1):
            # Iterate through each number in the given list nums
            for num in nums:
                # Check if it's possible to subtract num from the current sum i
                if i - num >= 0:
                    # Add the number of combinations to dp[i] by using dp[i - num]
                    dp[i] += dp[i - num]
                    
        # The final result is stored in dp[target], which represents the
        # number of combinations to make the target sum
        return dp[target]
