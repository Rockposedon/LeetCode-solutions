class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Remove leading and trailing whitespaces from the string
        s = s.strip()
    
        # Define the set of valid sign characters
        signs = {'-', '+'}
    
        # Initialize an empty string to store the resulting number
        res = ''
    
        for char in s:
            # Check if the character is a valid sign and no digits have been encountered yet
            if char in signs and not res:
                res += char
            
            elif char.isnumeric():
                res += char
            else:
                
                break
            
        # Check if the resulting string is empty or contains only sign characters
        if not res or res in signs:
            return 0
    
        # Convert the resulting string to an integer and bound it within the 32-bit signed integer range
        return max(min(int(res), 2**31 - 1), -2**31)
