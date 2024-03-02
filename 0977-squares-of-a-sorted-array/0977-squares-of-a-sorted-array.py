class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        new_square = []
        for i in range(0,n):
            a = nums[i]**2
            new_square.append(a)
            new_square.sort()
            
        return new_square
            
        