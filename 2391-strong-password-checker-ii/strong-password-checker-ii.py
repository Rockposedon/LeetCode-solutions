class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        firstLetter = ""

        lower, upper, digit, special  = [False] * 4

        if len(password) < 8:
            return False

        for let in password:
            if let.islower():
                lower = True
            if let.isupper():
                upper = True
            if let in ('0123456789'):
                digit = True
            if let == firstLetter:
                return False
            if let in ("!@#$%^&*()-+"):
                special = True
            firstLetter = let
        
        return lower and upper and digit and special