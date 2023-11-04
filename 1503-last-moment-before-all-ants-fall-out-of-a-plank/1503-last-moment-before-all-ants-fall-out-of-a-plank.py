# class Solution:
#     def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
#         if left is None and right is None :
#             return 0


#         # If there are ants on the left side only, the last moment is the maximum position of ants on the left side.
#         elif left and not right:
#             return max(left)

#         # If there are ants on the right side only, the last moment is the maximum position of ants on the right side.
#         elif right and not left:
#             return n - min(right)

#         l = -1
#         r = -1

#         # Find the maximum position of ants on the left side.
#         for left_index in left:
#             l = max(l, left_index)

#         # Find the maximum position of ants on the right side. Note that we subtract the minimum right position from n.
#         for right_index in right:
#             r = max(r, right_index)

#         # The last moment is determined by the maximum position between left and right sides.
#         return max(l,r)

class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        # no ants, no time! 
        if left is None and right is None : 
            return 0 
        elif left and not right : 
            # only got ants heading left, we need the maximal position of that lefty 
            return max(left)
        elif right and not left : 
            return n - min(right)


        left_max = -1
        right_max = -1 
        for left_index in left :
            left_max = max(left_max, left_index)
        for right_index in right : 

            right_max = max(right_max, n-right_index)

        return max(left_max, right_max)