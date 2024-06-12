class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        # Use a dictionary to store the last index of each element
        index_map = {}
        
        for i, num in enumerate(nums):
            if num in index_map and i - index_map[num] <= k:
                return True
            # Update the last index of the current element
            index_map[num] = i
            
        return False