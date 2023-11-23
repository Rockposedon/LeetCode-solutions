class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        # result list to store boolen value after checking arithematic subarray
        result = []
        
        # iterating over range defined by l and r 
        for i in range(len(l)):
            
            # sorting the sub array based on range [l[i], r[i]+1]
            sub_array = sorted(nums[l[i]:r[i]+1])
            
            # I have write function to check the sub array is arithemtic sub array 
            bool_value = self.arith_progression(sub_array)
            
            # Adding result based on arith_progression function
            result.append(bool_value)
            
        # This is our Final output
        return result
    
    def arith_progression(self,arr) :
        
        # Finding common difference between two consecutive elements
        common_difference = arr[1]-arr[0]
        
        # Iterate over sub array to check arithmetic sub array 
        for i in range(2,len(arr)):
            if arr[i] - arr[i-1] != common_difference:
                # if sub array is not arithmetic sub array, return flase
                return False
        # when sub array is arithmetic sub array, return true
        return True
        
