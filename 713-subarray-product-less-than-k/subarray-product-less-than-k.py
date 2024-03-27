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