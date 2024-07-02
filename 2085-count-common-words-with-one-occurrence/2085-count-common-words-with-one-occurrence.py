class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        
        # Initialize a counter to keep track of words that appear exactly once in both lists
        count = 0
        
        # Create Counters for words1 and words2
        c1 = Counter(words1)
        c2 = Counter(words2)
        
        # Iterate through each unique word in words1 (using c1.keys())
        for word in c1:
            
            # Check if the word appears exactly once in both words1 and words2
            if c1[word] == 1 and c2[word] == 1:
                
                # Increment the count if the conditions are met
                count += 1
        
        # Return the total count of words that appear exactly once in both lists
        return count