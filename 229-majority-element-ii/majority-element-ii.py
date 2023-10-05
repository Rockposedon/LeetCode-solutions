#                                                     Approach One 

# class Solution:
#     def majorityElement(self, nums: List[int]) -> List[int]:
#         freq={}
#         ans=[]
#         for i in range(0,len(nums)):
#             if(nums[i] in freq):
#                 freq[nums[i]]+=1
#             else:
#                 freq[nums[i]]=0
#         for i in freq:
#             if freq[i]>=len(nums)//3:
#                 ans.append(i)
#         return ans



#                                                     Approach Two


# from collections import Counter
# class Solution:
#     def majorityElement(self, nums: List[int]) -> List[int]:
#         num = list(set(nums))
#         ls = []
#         for i in num:
#             d = nums.count(i)
#             if d > len(nums) // 3:
#                 ls.append(i)
#         return ls

#                                          Using Boyer-Moore Majority Vote algorithm(use to find majority of element in array)

# class Solution:
#     def majorityElement(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         container1 = None
#         container2 = None
#         count1 = 0
#         count2 = 0
        
#         for i in nums :
#             if i == container1:
#                 count1 += 1
#             elif i == container2:
#                 count2 += 1
#             elif count1 == 0:
#                 container1 = i
#                 count1 += 1
#             elif count2 == 0:
#                 container2 = i
#                 count2 += 1
#             else :
#                 count1 -= 1
#                 count2 -= 1
            
#         count1,count2 = 0,0
            
#         result = []
#         for i in nums:
#             if i == container1:
#                 count1 += 1
#             elif i == container2:
#                 count2 += 1
        
#         if count1 > n//3:
#             result.append(container1)
#         elif count2 > n//3:
#             result.append(container2)
        
#         return result

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Initialize two candidate elements and their counters
        candidate1, candidate2 = None, None
        count1, count2 = 0, 0

        # First pass: Find the two most likely candidates
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 += 1
            elif count2 == 0:
                candidate2 = num
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1

        # Second pass: Count occurrences of the two candidates
        count1, count2 = 0, 0
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1

        result = []
        n = len(nums)

        # Check if candidates meet the requirement of appearing more than n/3 times
        if count1 > n // 3:
            result.append(candidate1)
        if count2 > n // 3:
            result.append(candidate2)

        return result

        