# Recursive Approach("Time Limit Exceed")
# class Solution:
#     def climbStairs(self, n: int) -> int:
        
#         if n == 1 :
#             return 1
        
#         if n ==2 :
#             return 2
        
#         return self.climbStairs(n-2)+self.climbStairs(n-1)

# DP Approach
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2 :
            return 2
        
        one = 1
        two = 1
        total = 0
        
        for i in range(n-1):
            total = one + two
            two = one
            one = total
            
        return total
