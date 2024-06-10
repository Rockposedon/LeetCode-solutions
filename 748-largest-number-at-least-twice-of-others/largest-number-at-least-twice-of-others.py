class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        
        # Find the largest number in the list
        largest = max(nums)
        
        # Find the index of the largest number
        maxIndex = nums.index(largest)
        
        # Check if the largest number is more than twice any other number
        for i in nums:
            
            # Skip the largest number itself
            if i!= largest and i*2 >largest:
                return -1
                
        # If no such number is found, return the index of the largest number
        return maxIndex