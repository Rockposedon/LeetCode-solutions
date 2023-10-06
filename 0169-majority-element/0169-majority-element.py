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
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         nums = sorted(nums)
#         n = len(nums)
#         return nums[n//2]

# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         dic = {}
#         for i in nums :
#             if i in dic:
#                 dic[i] += 1
#             else :
#                 dic[i] -= 1
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ele_dic = {}
    
        for i in nums:
        
            ele_dic[i] = ele_dic.get(i, 0) + 1
    
        for num, count in ele_dic.items():
            if count > len(nums) // 2:
                return num