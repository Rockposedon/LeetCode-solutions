"""class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        
        max_count = 0
        
        # Loop through each sentence in the list of sentences
        for sentence in sentences:
            # Split the sentence into words
            words = sentence.split()
            
            # Count the number of words in the sentence
            word_count = len(words)
            
            # Check if the word count is greater than max count, update max count by word count
            if max_count < word_count:
                max_count = word_count
        
        # Return the maximum word count found
        return max_count
"""
# Without split() funtion

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_count = 0
        for sentence in sentences:
            word_count = 0
            # Loop through each character in the sentence
            for char in sentence:
                # Check if the character is a space
                if char == ' ':
                    # Increment word count if a space is found
                    word_count += 1
            # Add 1 to word count to account for the last word (not followed by a space)
            word_count += 1
            # Update max_count if necessary
            if max_count < word_count:
                max_count = word_count
        return max_count
