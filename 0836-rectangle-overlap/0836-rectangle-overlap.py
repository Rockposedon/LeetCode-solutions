class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:

        [A,B,C,D], [E,F,G,H] = rec1, rec2
        if (F>=D or E>=C or B>=H or A>=G):
            return False
        elif F == H or E == G or B == D or A == C:
            return False
        return True        