class Solution:
    def countHomogenous(self, s: str) -> int:
        
        left = 0  # 'left' is the left pointer to the current homogenous substring
        
        res = 0   # 'res' will store the total count of homogenous substrings

        for right in range(len(s)):  # 'right' is the right pointer to the current character in the string
            
            if s[left] == s[right]:  # If the current character matches the leftmost character
            
                res += right - left + 1  # Increment the count by the length of the homogenous substring
            
            else:
            
                res += 1  # A different character is encountered, so increment the count by 1
            
                left = right  # Update 'left' to the current position

        return res % (10**9 + 7)  # Return the count modulo (10^9 + 7)
