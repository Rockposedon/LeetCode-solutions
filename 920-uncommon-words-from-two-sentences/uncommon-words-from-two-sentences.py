class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        

        s1 = s1.split(" ")  # Split s1 by space to get list of words
        s2 = s2.split(" ")  # Split s2 by space to get list of words
        
        result = []  
        
        # Create Counters for both lists of words
        c1 = Counter(s1)
        c2 = Counter(s2)
        
        # Combine counters to get total counts of words across both sentences
        counter = c1 + c2
        
        # Iterate through each word in the combined counter
        for word in counter:
            # Check if the word appears exactly once in the combined sentences
            if counter[word] == 1:
                result.append(word)  # Add the word to result list if it's uncommon
        
        return result