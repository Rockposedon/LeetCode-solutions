class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        if len(word1) != len(word2):
            return False

        # Function to count occurrences of characters in a word
        def count_occurrences(word):
            char_count = {}
            for char in word:
                char_count[char] = char_count.get(char, 0) + 1
            return char_count

        # Count occurrences of characters in both words
        c1 = count_occurrences(word1)
        c2 = count_occurrences(word2)

        # Check if the sets of characters are the same
        if set(c1.keys()) != set(c2.keys()):
            return False

        # Check if the sorted lists of character counts are the same
        return sorted(c1.values()) == sorted(c2.values())