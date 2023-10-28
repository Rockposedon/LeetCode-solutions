# Approach 1st

# class Solution:
#     def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:

#         [A,B,C,D], [E,F,G,H] = rec1, rec2
#         if (F>=D or E>=C or B>=H or A>=G):
#             return False
#         elif F == H or E == G or B == D or A == C:
#             return False
#         return True        


# Approach 2nd
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        """
        the idea here is to check the cases where no overlap. 
        """
        x1, y1, x2, y2 = rec1
        x11, y11, x22, y22 = rec2

        if y11 >= y2 or y22 <= y1 or x11 >= x2 or x22 <= x1:
            return False # no overlap

        return True     # there is an overlap