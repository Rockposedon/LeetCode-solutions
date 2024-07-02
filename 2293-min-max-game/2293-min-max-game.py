class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        
        # Continue looping until there is only one element left in nums
        while len(nums) > 1:
            
            newNums = []  
            n = len(nums)  
            
            # Iterate over half of the current length of nums
            for i in range(n // 2):
                
                if i % 2 == 0:
                    # For even indices, append the minimum of the pair
                    newNums.append(min(nums[2 * i], nums[2 * i + 1]))
                else:
                    # For odd indices, append the maximum of the pair
                    newNums.append(max(nums[2 * i], nums[2 * i + 1]))
            
            # Update nums to newNums for the next iteration
            nums = newNums
        
        # Return the single remaining element in nums
        return nums[0]
