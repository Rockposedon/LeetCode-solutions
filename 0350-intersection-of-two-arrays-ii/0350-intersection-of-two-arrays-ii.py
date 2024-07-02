class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Initialize the result list to store the intersection
        result = []
        
        # Iterate through each element in nums1
        for i in nums1:
            # Check if the current element is in nums2
            if i in nums2:
                # If it is, append it to the result list
                result.append(i)
                # Remove the element from nums2 to handle duplicates correctly
                nums2.remove(i)
        
        # Return the result list containing the intersection of nums1 and nums2
        return result