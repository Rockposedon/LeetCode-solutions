"""Time limit exceed"""
# class Solution:
#     def countNicePairs(self, nums: List[int]) -> int:
#         # Define the modulus value
#         mod = 10 ** 9 + 7
        
#         # Get the length of the input array
#         n = len(nums)
        
#         # Initialize a variable to count the nice pairs
#         nice_pair = 0
        
#         # Iterate through each pair of indices i, j
#         for i in range(0, n):
#             for j in range(i + 1, n):
#                 # Reverse the digits of nums[i] and nums[j]
#                 rev_i = int(str(nums[i])[::-1])
#                 rev_j = int(str(nums[j])[::-1])
                
#                 # Check if swapping digits results in equal sums
#                 if nums[i] + rev_j == nums[j] + rev_i:
#                     nice_pair += 1

#         # Return the count of nice pairs modulo mod
#         return nice_pair % mod
                    
   
"""Another approach using Counter from Collection module"""

class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        mod = 10 ** 9 + 7
        n = len(nums)
        
        # Create a Counter to store the frequency of differences
        difference_counter = Counter()
        
        # Initialize a variable to count the nice pairs
        nice_pair = 0
        
        # Iterate through each number in the nums array
        for num in nums:
            # Reverse the digits of the current number
            rev_num = int(str(num)[::-1])
            
            # Calculate the difference between the number and its reverse
            diff = num - rev_num
            
            # Increment the count for the current difference in the Counter
            nice_pair += difference_counter[diff]
            
            # Update the Counter with the current difference
            difference_counter[diff] += 1

        # Return the count of nice pairs modulo mod
        return nice_pair % mod                         