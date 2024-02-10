class Solution:
    def countSubstrings(self, s: str) -> int:
        # List to store all possible substrings
        substrings = []

        # Step 1: Generate all Substrings
        for i in range(len(s) + 1):
            for j in range(i):
                # Append substring s[j:i] to the list
                substrings.append(s[j:i])

        # Counter for palindromic substrings
        count = 0

        # Step 2: Count Palindromic Substrings
        for substring in substrings:
            # Check if the substring is a palindrome
            if substring == substring[::-1]:
                count += 1

        # Step 3: Return the final count
        return count