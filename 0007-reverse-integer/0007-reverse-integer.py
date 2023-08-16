class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        string_int = str(abs(x))[::-1]
        
        if int(string_int) > 2 ** (31):
            string_int = '0'
        elif x < 0 :
            string_int = '-'+string_int
        return (int(string_int))
    
    
    

        
