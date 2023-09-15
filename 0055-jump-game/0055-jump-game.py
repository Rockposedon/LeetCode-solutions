from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        max_reach = 0
        
        for i in range(n):
            # If index is beyond the maximum reach, return False
            if i > max_reach:
                return False
            
            # Update the reach
            max_reach = max(max_reach, i + nums[i])
        
        # If the reach is greater than or equal to the last index, return True
        return max_reach >= n - 1
        