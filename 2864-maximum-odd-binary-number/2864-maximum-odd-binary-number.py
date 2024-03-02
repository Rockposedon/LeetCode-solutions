class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count_one = 0
        count_zero = 0
        for i in range(0,len(s)):
            if s[i] == '1':
                count_one += 1
            elif s[i] == '0':
                count_zero += 1
        return '1' * (count_one-1) + '0' * count_zero + '1'

    