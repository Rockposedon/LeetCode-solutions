class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums_sort = sorted(nums, reverse = True)
        return nums_sort[k-1]
    
        
        