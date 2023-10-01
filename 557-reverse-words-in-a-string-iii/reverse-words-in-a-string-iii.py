# 1st Approach
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        
        # spliting up the strng 
        n=s.split()
        
        # empty list to return result in it 
        b=[]
        
        # traverse in strng
        for i in n:
            b.append(i[::-1])
        
        # join the word and return it    
        return " ".join(b)
'''
# 2nd Approach
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s[::-1]
        s = s.split(" ")
        s = s[::-1]
        return " ".join(s)
        
