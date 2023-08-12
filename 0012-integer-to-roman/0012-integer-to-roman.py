class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

        result = ""

        # Iterate through the symbols and their corresponding values
        for i in range(len(roman)):
            while num >= values[i]:
                # Append the current symbol to the result and subtract its value from num
                result += roman[i]
                num -= values[i]

        return result
        