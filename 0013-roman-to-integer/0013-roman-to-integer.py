class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}

        s = s.replace("IV","IIII").replace("IX","IIIIIIIII").replace("XL", "XXXX").replace("XC", "XXXXXXXXX").replace("CD", "CCCC").replace("CM", "CCCCCCCCC")

        # Initialize a variable to store the result of the conversion
        res = 0

        # Iterate through each character in the modified Roman numeral string
        for char in s:
            # Add the value corresponding to the current Roman numeral to the result
            res += a[char]

        # Return the final result of the conversion
        return res
        
        