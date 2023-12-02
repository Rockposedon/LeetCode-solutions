class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        ans = ''  # Initialize a string to store valid words
        
        # Iterate through each word in the list
        for word in words:
            
            # Check if the word can be formed using the characters in 'chars'
            for letter in word:
                
                if chars.count(letter) < word.count(letter):
                    break  # If the word cannot be formed, break out of the loop
            else:
                ans += word  # If the word can be formed, add it to the result string
        
        return len(ans)  # Return the length of the concatenated valid words