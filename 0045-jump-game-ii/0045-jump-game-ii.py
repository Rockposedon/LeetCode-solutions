from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0           
        curr_pos = 0        
        max_reach = 0       
        
        for i in range(len(nums) - 1):
            max_reach = max(max_reach, i + nums[i])  # Update the maximum reachable position
            
            # If we at current position we have to jump
            if i == curr_pos:  
                jumps += 1            # Increment number of jumps
                curr_pos = max_reach  # Update the current position to the maximum reachable position
        
        return jumps  # Return the total number of jumps required
