class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        
        sums = 0
        res = 0
        for i in nums:
            sums += i
            if sums == 0:
                res += 1
        return res

