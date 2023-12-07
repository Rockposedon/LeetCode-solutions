class Solution:
    def largestOddNumber(self, s: str) -> str:
        # Get the length of the input string
        n = len(s)

        # Iterate through the string from right to left
        for i in range(n - 1, -1, -1):
            # Convert the current character to an integer
            a = int(s[i])

            # Check if the integer is odd
            if a % 2 != 0:
                # If odd, return the substring from the beginning of the string up to the current position
                return s[:i + 1]

        # If no odd digit is found, return an empty string
        return ""