class Solution:
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
