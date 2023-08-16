
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1.extend(nums2)
        nums1.sort()
        n=len(nums1)//2

        if(len(nums1)%2==0):
            return (float(nums1[n]+nums1[n-1]))/2
        else:
            return float(nums1[n])