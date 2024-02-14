class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for i in range(0,len(words)):
            if words[i] == words[i][::-1]:
                return words[i]
            
        return ""