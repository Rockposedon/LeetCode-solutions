class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # Check for empty input
        if not nums:
            return []

        # Sort the array
        nums.sort()

        # Initialize a list of lists to store subsets
        result = [[num] for num in nums]
        
        for i in range(1, len(nums)):
            for j in range(i):
                # Check if the current number is divisible by the numbers in the previous subset
                if nums[i] % nums[j] == 0 and len(result[i]) < len(result[j]) + 1:
                    result[i] = result[j] + [nums[i]]

        # Find the subset with the maximum size
        maxSubset = max(result, key=len)

        return maxSubset