class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        triplets = []
        n = len(nums)

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicate values for i
        
            left = i + 1
            right = len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    triplets.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1  # Skip duplicate values for left
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1  # Skip duplicate values for right
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
    
        return triplets
            
        