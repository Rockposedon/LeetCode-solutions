class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        list1 = []
        list2 = []
        s1 = s.split()

        for i in pattern:
            list1.append(pattern.index(i))
        for i in s1:
            list2.append(s1.index(i))
        if list1 == list2:
            return True
        return False