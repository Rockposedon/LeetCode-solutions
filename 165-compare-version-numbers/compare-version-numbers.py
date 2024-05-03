class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        s1 = version1.split(".")
        s2 = version2.split(".")
        
        n = len(s1)
        m = len(s2)
        
        for i in range(n):
            s1[i] = int(s1[i])
        for i in range(m):
            s2[i] = int(s2[i])
        
        length = min(n,m)
        for i in range(length):
            if s1[i] < s2[i]:
                return -1
            if s1[i] > s2[i]:
                return 1
            
        if sum(s1) < sum(s2):
            return -1
        if sum(s1) > sum(s2):
            return 1
        
        return 0
