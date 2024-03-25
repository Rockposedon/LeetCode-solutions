class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        a = set()
        b = []
        for i in nums:
            if i in a:
                b.append(i)
            a.add(i)
        return b