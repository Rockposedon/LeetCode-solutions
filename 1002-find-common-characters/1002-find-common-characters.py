class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # Initialize min_freq with the character count of the first word
        min_freq = Counter(words[0])
        
        # Iterate over each word in the list
        for i in words:
            # Update min_freq to keep only the minimum frequency of each character
            # that is common in min_freq and the current word
            min_freq &= Counter(i)
        
        # Return the list of common characters with their counts
        return list(min_freq.elements())