class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        # Check if lengths of the two strings are equal
        if len(s) != len(goal):
            return False

        # If the two strings are equal, check if there are duplicate characters
        if s == goal and len(set(s)) < len(s):
            return True

        # Keep track of differing indices
        diffs = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                diffs.append(i)

        # Check if there are exactly two differing indices
        if len(diffs) == 2:
            i, j = diffs
            if (s[i], s[j]) == (goal[j], goal[i]):
                return True

        return False