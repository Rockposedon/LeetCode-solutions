class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # Find the first decreasing element from the end (index 'i')
        i = j = len(nums) - 1
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1

        # If a decreasing element is found
        if i > 0:
        # Find the smallest element to the right of 'i-1' that is larger than 'nums[i-1]'
        
            while nums[j] <= nums[i - 1]:
                j -= 1
    
            # Swap 'nums[i-1]' and 'nums[j]'
            nums[i - 1], nums[j] = nums[j], nums[i - 1]

        # Reverse the elements to the right of index 'i'
        nums[i:] = nums[i:][::-1]
        