class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # covert string s into lower case
        s_lower = s.lower()
        
        # removing non-alphanumeric characters
        s_replace = ""
        for i in s_lower:
            if i.isalnum():
                s_replace += i
                
        # compare s_replace with its reverse 
        if s_replace == s_replace[::-1]:
            return True
        else :
            return False
        