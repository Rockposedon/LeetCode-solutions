class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        char_set = set()
        result = 0 
        
        # Loop over charters in string s
        for i in s :
            
            # If set already contains character
            if i in char_set:
                # Reomve that character
                char_set.remove(i)
                # Add 2 occurences to plaindrome
                result += 2
            else:
                # If not present, add character to set 
                char_set.add(i)
                
        # If there are any characters left in the set, it means they have odd counts
        # We can place one of these characters in the middle of the palindrome      
        if char_set:
            result += 1
        return result 