class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        nums.sort()
        left = 0
        right = len(nums)-1
        
        while left < right:
            
            mid  = (left + right) // 2
            if nums[mid] < (mid +1):
                right = mid
            else :
                left= mid +1
            
        return nums[left]
                
            
