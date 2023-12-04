class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = ''  # Variable to store the largest consecutive substring
        cnt = 1    # Counter to keep track of the consecutive characters count
        
        # Iterate through the characters of the string, starting from the second character
        for i in range(1, len(num)):
            # Check if the current character is the same as the previous one
            if num[i] == num[i - 1]:
                cnt += 1  # Increment the consecutive characters count
            else:
                cnt = 1   # Reset the count if the characters are different
            
            # Check if three consecutive characters are found
            if cnt == 3:
                res = max(res, num[i] * 3)  # Update the largest substring if necessary
        
        return res  # Return the largest consecutive substring
