class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        # Sort the words by length
        words.sort(key=len)

        # Initialize a dictionary to store the longest chain length for each word
        dp = {}
        maxChainLength = 0

        # Iterate through each word in the sorted list
        for word in words:
            dp[word] = 1  # Initialize with a minimum chain length of 1

            # Try removing each character one at a time
            for i in range(len(word)):
                temp = word[:i] + word[i + 1:]
                if temp in dp:
                    dp[word] = max(dp[word], dp[temp] + 1)

            # Update the maximum chain length
            maxChainLength = max(maxChainLength, dp[word])

        return maxChainLength