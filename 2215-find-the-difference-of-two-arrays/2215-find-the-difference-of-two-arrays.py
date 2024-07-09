class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        set1 = set(nums1)
        set2 = set(nums2)
        
        # Initialize the lists for storing the differences
        diff1 = []
        diff2 = []
        
        # Find elements in nums1 that are not in nums2
        for x in set1:
            if x not in set2:
                diff1.append(x)
        
        # Find elements in nums2 that are not in nums1
        for x in set2:
            if x not in set1:
                diff2.append(x)
        
        # Return the results as a 2D list
        return [diff1, diff2]