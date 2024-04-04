class Solution:
    def maxDepth(self, s: str) -> int:
        level = 0
        max_depth = 0
        for c in s:
            level += c == '('
            max_depth = max(max_depth, level)
            level -= c == ')'
        return max_depth