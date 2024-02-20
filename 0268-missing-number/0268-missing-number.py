class Solution:
    def missingNumber(self, nums: List[int]) -> int:
# '''        nums.sort()
#         l = nums[-1]
#         for i in range(0,l+2):
#             if i not in nums :
#                 return i
#         return -1
# '''   
        nums_set = set(nums) 
        l = max(nums)
        for i in range(0,l+2):
            if i not in nums_set:
                return i 
            
        return -1