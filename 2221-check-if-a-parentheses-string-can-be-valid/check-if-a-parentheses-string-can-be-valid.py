class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if len(s) % 2 == 1:
            return False
        
        # From Left to Right balancing "("
        balance = 0
        for i in range(n):
            if s[i] == '(' or locked[i] == '0':
                balance += 1
            else :
                balance -= 1
            if balance < 0:
                return False
        
        # From Right to Left balancing ")"
        balance = 0
        for i in range(n-1,-1,-1):
            if s[i] == ')' or locked[i] == '0':
                balance += 1
            else:
                balance -= 1
            if balance < 0:
                return False 
        return True

        
