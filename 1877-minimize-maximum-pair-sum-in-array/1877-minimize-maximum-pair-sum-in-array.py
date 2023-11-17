# class Solution:
#     def minPairSum(self, nums: List[int]) -> int:
#         # Sort the array in ascending order
#         nums.sort()
        
#         # Initialize pointers for the start and end of the sorted array
#         start = 0
#         end = len(nums) - 1
        
#         # Initialize variable to track the maximum pair sum
#         max_sum = 0
        
#         # Pair elements from the two ends of the sorted array
#         while start < end:
#             # Calculate the pair sum for the current pair
#             result = nums[start] + nums[end]
            
#             # Move the pointers inward
#             start += 1
#             end -= 1
            
#             # Update the maximum pair sum if the current pair sum is greater
#             if result > max_sum:
#                 max_sum = result
        
#         # Return the minimized maximum pair sum
#         return max_sum



""" Another 
    approach dividing list into two halves and sort another list in reverse order then find sum"""
    
    
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        
        nums.sort()
        mid = len(nums) // 2
        first_list = nums[:mid]
        second_list = nums[mid:]
        

        # Sort the second list in descending order
        second_list_sorted_desc = sorted(second_list, reverse=True)

        # Pair up the elements
        pairs = zip(first_list, second_list_sorted_desc)

        # Find the maximum pair sum
        max_pair_sum = max(pair[0] + pair[1] for pair in pairs)

        return max_pair_sum
