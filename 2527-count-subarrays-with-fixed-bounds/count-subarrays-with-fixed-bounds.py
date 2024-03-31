class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        n = len(nums)
        count = 0
        min_count = -1
        max_count = -1
        leftBound = -1
        
        for i in range(n):
            if nums[i] < minK or nums[i] > maxK:
                leftBound = i
            if nums[i] == minK:
                min_count = i
            if nums[i] == maxK:
                max_count = i
            
            count += max(0,min(min_count,max_count)-leftBound)
        return count