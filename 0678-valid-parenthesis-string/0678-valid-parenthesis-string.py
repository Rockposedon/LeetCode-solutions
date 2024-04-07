class Solution:
    def checkValidString(self, s: str) -> bool:
        
        '''
        c1 is for left Parenthesis count
        c2 is for right Parenthesis count
        '''
        
        c1 = c2 = 0
        for i in s:
            if i == '(':
                c1 += 1
                c2 += 1
            elif i == ')':
                c1 -= 1
                c2 -= 1
            else:
                c1 -= 1
                c2 += 1
            if c2 < 0:
                return False
            if c1 < 0:
                c1 = 0
        return c1 == 0
