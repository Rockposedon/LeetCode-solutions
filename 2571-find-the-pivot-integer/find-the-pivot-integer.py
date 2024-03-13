# class Solution:
#     def pivotInteger(self, n: int) -> int:
#         if n == 1:
#             return 1
#         if n == 8:
#             return 6
#         if n == 49:
#             return 35
#         if n == 288:
#             return 204
#         return -1 
class Solution:
    def pivotInteger(self, n: int) -> int:
        for i in range(1,n+1):
            sum_left = sum(range(1,i+1))
            sum_right = sum(range(i,n+1))
            if sum_left == sum_right:
                return i
        return -1
