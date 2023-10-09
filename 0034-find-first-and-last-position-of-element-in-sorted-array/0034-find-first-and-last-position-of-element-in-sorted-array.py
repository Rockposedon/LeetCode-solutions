class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        start = -1 # setting starting index as -1
        end = -1   # setting ending index as -1
        
        for i in range(n) :
            if nums[i] == target: # when traversing from left to right, if target element is foound in nums
                start  = i        # set starting index to current index 
                break
                
        if start == -1: # base case 
            return [-1,-1]
        
        
        for j in range(n-1,-1,-1): # when traversing from right to left , if target element is found in nums
            if nums[j] == target:  # set ending index to current element index
                end = j
                break
                
        return [start,end]