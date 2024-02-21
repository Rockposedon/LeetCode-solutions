class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        while right>left:
            # turn off rightmost 1-bit
            right = right&(right-1)
        return right&left
