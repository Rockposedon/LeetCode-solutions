class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # Combine the two lists nums2 into nums1
        nums1.extend(nums2)

        nums1.sort()
        l = len(nums1)
        # Index of the middle element
        n = len(nums1) // 2

        if l % 2 == 0:
            # If the combined list has an even number of elements, median will be average of the two middle elements
            return float(nums1[n] + nums1[n-1]) / 2
        else:
            # If the combined list has an odd number of elements, the median is the middle element
            return float(nums1[n])