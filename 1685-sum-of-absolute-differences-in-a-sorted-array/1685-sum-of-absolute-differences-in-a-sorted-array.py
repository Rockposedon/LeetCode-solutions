from typing import List

class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        # Initialize an array for prefix sums
        prefix_sum = [0] * n  
        
        # Initialize an array for suffix sums
        suffix_sum = [0] * n  

        # Calculate prefix sum
        prefix_sum[0] = nums[0]
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]

        # Calculate suffix sum
        suffix_sum[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + nums[i]

        result = []  # Initialize an empty list to store the final results

        # Calculate absolute differences for each element
        for i in range(n):
            # Step 3.1: Calculate left sum efficiently using prefix sum
            left_sum = i * nums[i] - prefix_sum[i]

            # Calculate right sum efficiently using suffix sum
            right_sum = suffix_sum[i] - (n - i - 1) * nums[i]

            # Calculate the total sum of absolute differences
            result.append(left_sum + right_sum)

        # Return the final result
        return result
    
    
    """Time Complexity : O(n)"""
