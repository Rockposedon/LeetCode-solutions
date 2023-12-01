class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        
        result1 = " "
        result2 = " "
        
        for i in word1:
            result1 += i
        
        for j in word2:
            result2 += j
            
        if result1 != result2:
            return False
        else :
            return True
            
        