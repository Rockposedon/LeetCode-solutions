class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        
        # Dictionary to store the frequency of each element
        freq = {}  
        
        # Iterate through each subarray
        for subarr in nums:
            for ele in subarr:
                
                # Increment the count of the element in the dictionary
                if ele in freq:
                    freq[ele] += 1
                else:
                    freq[ele] = 1
        # List to store the common elements
        result = []  
        
        # Check which elements appear in all subarrays
        for ele, count in freq.items():
            if count == len(nums):
                result.append(ele)
        
        # Return the sorted list of common elements
        return sorted(result)