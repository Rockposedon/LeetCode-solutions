class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Initialize the result list to store the unique intersection
        result = []
        
        # Iterate through each element in nums1
        for i in nums1:
            # Check if the current element is in nums2
            if i in nums2:
                # Ensure the element is added to the result only once
                if i not in result:
                    result.append(i)
        
        # Return the result list containing the unique intersection of nums1 and nums2
        return result