# <------------------------------Using Boyer Moore Majority vote algorithm------------------------------------------------>


# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
        
#         count=0
#         result=0
        
#         for n in nums:
#             if count==0:
#                 result=n
#             if n==result:
#                 count+=1
#             else:
#                 count-=1
#         return result

                
# <-----------------------------another approach using sort and len ----------------------------------------------------->
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums = sorted(nums)
        n = len(nums)
        return nums[n//2]