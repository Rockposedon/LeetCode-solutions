class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        # Dictionary to store character counts
        counts = {}
        
        # Iterate through each word in the list
        for word in words:
            # Count occurrences of each character in the current word
            for c in word:
                counts[c] = counts.get(c, 0) + 1
        
        # Get the total number of words in the list
        n = len(words)
        
        # Check if the count of each character is a multiple of the total number of words
        for val in counts.values():
            if val % n != 0:
                # If any character count is not a multiple, it's not possible to make all words equal
                return False
        
        # If all character counts are multiples of the total number of words, return True
        return True
