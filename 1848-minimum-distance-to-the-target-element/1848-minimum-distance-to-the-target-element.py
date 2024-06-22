class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
    
        n = len(nums)    
        min_distance = float('inf')
        
        for i in range(0, n):
            # Check if the current element is equal to the target
            if nums[i] == target:
                # Calculate the distance from the current index to the start index
                distance = abs(i - start)
                
                # Update min_distance with the smaller value 
                min_distance = min(min_distance, distance)
        
        # Return the minimum distance found
        return min_distance