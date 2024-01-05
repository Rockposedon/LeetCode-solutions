class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        # Check if the input list is empty
        if not nums or len(nums) == 0:
            return 0
        
        # Get the length of the input list
        n = len(nums)
        
        # Initialize an DP array to store the length of the longest increasing subsequence ending at each index
        dp = [1] * n
        
        # Iterate through the list to calculate the length of the element at each index
        for i in range(1, n):
            
            for j in range(i):
                # If the current number is greater than the number at index j
                
                if nums[i] > nums[j]:
                    
                    # update the length of dp at index i
                    dp[i] = max(dp[i], dp[j] + 1)
        
        # Initialize a variable to store the maximum length of LIS
        max_count = 1
        
        # Iterate through the dp array to find the maximum length
        for length in dp:
            max_count = max(max_count, length)
        
        # Return the maximum length of the increasing subsequence
        return max_count