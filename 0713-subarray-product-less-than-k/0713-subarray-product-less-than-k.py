"""
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0
        product = 1
        left = 0
        
        for right in range(n):
            product *= nums[right]
            
            while product >= k and left <= right:
                product /= nums[left]
                left += 1
            
            count += right - left + 1
        
        return count
"""
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        product = 1
        count = 0
        n = len(nums)
        while right < n :
            product *= nums[right]
            while product >= k and left <= right:
                product //= nums[left]
                left += 1
            count += (right-left) + 1
            right += 1
        return count 





































































