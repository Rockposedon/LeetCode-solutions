class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        
        # length of binary string in array
        n = len(nums)
        
        # creating binary string for ones and zeros of lenght n 
        zeros = "0" * n
        ones =  "1" * n
        
        # check if zeros is not present in array
        if zeros not in nums:
            return zeros
        
        # check if ones is not present in array
        if ones not in nums:
            return ones
        
        # iterate through each binary string
        for b_string in nums:
            
            # Check if the reverse of b_string is not in nums, return the reversed string
            if b_string[::-1] not in nums:
                return b_string[::-1]
            
         # when above all condition are not met return "01"  
        return "01"

            
