class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        
        n = len(nums)
        if n == 1:
            return True
        for i in range(n-1):
            sums = nums[i] + nums[i+1]
            if sums % 2 == 0:
                return False
        return True       