class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        # Initialize two pointers i and j to 0
        i = j = 0
        
        # Loop through both strings until we reach the end of either string
        while i < len(s) and j < len(t):
            
            # If the current character in s matches the current character in t
            if t[j] == s[i]:
                
                # Move to the next character in t
                j += 1
                
            # Always move to the next character in s
            i += 1
        
        # Return the number of characters in t that were not matched in s
        return len(t) - j
