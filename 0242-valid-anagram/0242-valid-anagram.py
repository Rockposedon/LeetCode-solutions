class Solution(object):
    def isAnagram(self, s, t):
        
        # In case of different length of thpse two strings
        if len(s) != len(t):
            
            return False
        
        for idx in set(s):
            
            # Compare s.count(l) and t.count(l) for every index i from 0 to 26
            # If they are different, return false
            if s.count(idx) != t.count(idx):
                return False
        return True     