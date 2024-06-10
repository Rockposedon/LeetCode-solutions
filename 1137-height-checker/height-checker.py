class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        hs = sorted(heights)
        if heights == hs:
            return 0
        count = 0
        for i in range(len(heights)):
            if heights[i] != hs[i]:
                count += 1
            pass
        return count