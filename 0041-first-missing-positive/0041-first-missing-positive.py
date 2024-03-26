class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        seen = [False]*(n+1)
        
        for i in nums:
            if 0 < i <= n :
                seen[i] = True
        
        for j in range(1,n+1):
            if not seen[j]:
                return j
        
        return n+1