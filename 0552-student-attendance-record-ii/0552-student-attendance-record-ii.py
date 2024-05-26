class Solution:
    def checkRecord(self, n: int) -> int:
        # Initial state for dp array
        # dp[0]: 0 Absences, 0 Late
        # dp[1]: 0 Absences, 1 Late
        # dp[2]: 0 Absences, 2 Late
        # dp[3]: 1 Absence, 0 Late
        # dp[4]: 1 Absence, 1 Late
        # dp[5]: 1 Absence, 2 Late
        dp = [1, 1, 0, 1, 0, 0]  
        mod = int(1e9) + 7  

        # Iterate for each day from 1 to n-1
        for _ in range(n - 1):
            # Calculate the number of valid sequences ending with:
            # Sum of all sequences without 'A' and with 0, 1, or 2 'L' ending today
            noA_noL = sum(dp[:3]) % mod  # Present today
            # All sequences that had no 'L' yesterday, now ending with one 'L'
            noA_oneL = dp[0]  # Late today
            # All sequences that had one 'L' yesterday, now ending with two 'L'
            noA_twoL = dp[1]  # Late today
            # Sum of all sequences, since we can have one 'A' in the sequence
            oneA_noL = sum(dp) % mod  # Present today
            # All sequences that had no 'L' and one 'A' yesterday, now ending with one 'L'
            oneA_oneL = dp[3]  # Late today
            # All sequences that had one 'L' and one 'A' yesterday, now ending with two 'L'
            oneA_twoL = dp[4]  # Late today

            # Update dp array with new values
            dp = [noA_noL, noA_oneL, noA_twoL, oneA_noL, oneA_oneL, oneA_twoL]

        # Return the sum of all valid sequences mod 1e9+7
        return sum(dp) % mod
