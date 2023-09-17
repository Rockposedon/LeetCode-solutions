class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        set1= set(nums)
        i = 1

        # checking membership of each element
        while i in set1:
            i += 1
        return i
        