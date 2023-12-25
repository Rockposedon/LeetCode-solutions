class Solution:
    def numDecodings(self, s: str) -> int:
        # Dictionary to store the results of subproblems for dynamic programming
        dp = {}
        # Length of the input string
        length = len(s) - 1

        # Recursive function to calculate the number of decodings
        def getResult(index):
            # If the current index exceeds the length of the string, there is only one way to decode (empty string)
            if index > length:
                return 1
            # If the current digit is '0', it cannot be decoded alone
            if s[index] == '0':
                return 0
            # If the result for the current index is already calculated, return it
            if index in dp:
                return dp[index]
            
            # Calculate the number of decodings for a single letter (current digit)
            singleLetter = getResult(index + 1)
            
            # Calculate the number of decodings for a two-letter word (current digit and the next digit)
            word = 0
            if index < length and int(s[index] + s[index + 1]) <= 26:
                word = getResult(index + 2)
            
            # Save the result for the current index and return it
            dp[index] = singleLetter + word
            return dp[index]

        # Call the recursive function starting from the first digit (index 0)
        return getResult(0)