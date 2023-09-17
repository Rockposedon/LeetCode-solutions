class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        # using binary search
        
        nums.sort()
        
        # minimum and maximum of list 
        left = 0
        right = len(nums)-1
        
        # check list is not empty
        while left < right:
            # finding mid index of list 
            mid  = (left + right) // 2
            
            # check is there is duplicate on left
            if nums[mid] < (mid +1):
                right = mid
                
            # is there is duplicate on right
            else :
                left= mid +1
            
        return nums[left]
                
            
