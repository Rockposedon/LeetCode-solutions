class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        list1 = []
        list2 = []
        
        for i in s :
            list1.append(s.index(i))
            
        for j in t :
            list2.append(t.index(j))
            
        if list1 == list2:
            return True
        
        return False