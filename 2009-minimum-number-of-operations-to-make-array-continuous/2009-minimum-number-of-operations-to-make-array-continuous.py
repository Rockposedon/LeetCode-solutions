# class Solution:
#     def minOperations(self, nums: List[int]) -> int:

#         min_ele = nums[0]
#         for i in nums:
#             if i < min_ele:
#                 min_ele = i
#             mini = min_ele
            
            
#         max_ele = nums[0]
#         for i in nums:
#             if i > max_ele:
#                 max_ele = i
#             maxx = max_ele
            
#         if maxx - mini == len(nums) - 1:
#             return 0
     


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        nums.sort()
        
        left = 0 # the starting index of the current subsequence
        count = 1 # the current subsequence length
        max_count = 1 # the longest subsequence length
        
        for i in range(1, len(nums)):
            # to avoid counting duplicate values in the window size
            if nums[i] != nums[i - 1]:
                count += 1

            # shrink the window from the left side so it remains valid
            while nums[i] - nums[left] > len(nums) - 1:
                # once again check to see if this was a duplicate
                if nums[left] != nums[left + 1]:
                    count -= 1
                left += 1
            max_count = max(count, max_count)
        
        return len(nums) - max_count
        
            
        