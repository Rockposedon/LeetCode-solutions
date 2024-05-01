class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        # Add characters to the result in the original order
        result = list(word)
        left = 0

        for right in range(len(word)):
            # We found ch - reverse characters up to ch by swapping
            if result[right] == ch:
                while left <= right:
                    result[right], result[left] = result[left], result[right]
                    left += 1
                    right -= 1
                return "".join(result)
        return word