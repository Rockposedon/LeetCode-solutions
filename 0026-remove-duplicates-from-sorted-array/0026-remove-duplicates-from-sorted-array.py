class Solution(object):
    def removeDuplicates(self, nums):
        
        
        # [:] is used to create same copy of the list
        
        nums[:] = sorted(set(nums))
        return len(nums)