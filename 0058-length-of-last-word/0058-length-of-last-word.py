class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # strip is used to remove spaces from begning and end 
        s = s.strip()
        
        # split is used to split string with space 
        s = s.split()
        
        #  slicing to use last word of string
        s = s[-1]
        
        # return the length of last word
        return len(s)
        