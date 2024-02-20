# class Solution:

#         """nums_set = set(nums) 
#         l = max(nums)
#         for i in range(0,l+2):
#             if i not in nums_set:
#                 return i 
            
#         return -1
#         """
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = (n * (n + 1)) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum