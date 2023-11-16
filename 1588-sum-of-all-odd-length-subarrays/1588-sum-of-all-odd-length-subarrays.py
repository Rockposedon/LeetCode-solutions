class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        
        sums = 0
        for i in arr:
            sums += i
        # as each subarray results in 1 element
        result = sums
        
        # Length of the array plus 1 for full array length
        length = len(arr)+1 
        
        # odd length
        for subarr_len in range(3,length , 2): 

            # Iterate through all starting positions of subarrays
            for start_index in range(length-subarr_len):

                # Calculate and add the sum of the current odd-length subarray
                result += sum(arr[start_index : start_index + subarr_len])

        return result

