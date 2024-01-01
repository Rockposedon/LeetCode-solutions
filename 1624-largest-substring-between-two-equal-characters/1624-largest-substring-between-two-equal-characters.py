class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        ans = -1  # Initialize the answer variable to store the maximum distance
        
        # Iterate through each character in the string as the potential left character
        for left in range(len(s)):
            # Iterate through characters to the right of the current left character
            for right in range(left + 1, len(s)):
                # If the characters at the current left and right indices are equal
                if s[left] == s[right]:
                    # Update the maximum distance if the current distance is greater
                    ans = max(ans, right - left - 1)
        
        # Return the maximum distance between equal characters
        return ans
