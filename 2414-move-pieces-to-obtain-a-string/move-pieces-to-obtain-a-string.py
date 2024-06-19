class Solution:
    def canChange(self, start: str, target: str) -> bool:
        # Remove all underscores and compare the remaining characters
        s = start.replace("_", "")
        t = target.replace("_", "")
        
        # If the sequences of 'L' and 'R' don't match, return False
        if s != t:
            return False

        left = 0  # Track the balance of 'L' characters
        right = 0  # Track the balance of 'R' characters
        
        # Iterate through characters of start and target strings simultaneously
        for i, j in zip(start, target):
            # Adjust balance for 'L' and 'R' in start
            if i == "L":
                left -= 1
            elif i == "R":
                right += 1
            
            # Adjust balance for 'L' and 'R' in target
            if j == "L":
                left += 1
            elif j == "R":
                right -= 1
        
            # If balance is negative for any character, return False
            if left < 0 or right < 0:
                return False
        
        # If all conditions are satisfied, return True
        return True

