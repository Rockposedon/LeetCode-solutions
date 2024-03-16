class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1]*n
        
        prefix_product = 1
        for i in range(n):
            result[i] = result[i]*prefix_product
            prefix_product = prefix_product * nums[i]
        
        suffix_product = 1
        for j in range(n-1,-1,-1):
            result[j] = result[j]*suffix_product
            suffix_product = suffix_product * nums[j]
        
        return result