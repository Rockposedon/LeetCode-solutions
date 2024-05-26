class Solution:
    def checkRecord(self, s: str) -> bool:
        count_A = 0
        count_L = 0
        for i in s:
            if i =='A':
                count_A += 1
                count_L = 0
            elif i == 'L':
                # Increment the count of consecutive 'L'
                count_L += 1
                # Check if there are 3 or more consecutive 'L'
                if count_L >= 3:
                    return False
            else:
                # Reset the count of consecutive 'L'
                count_L = 0
        
        # Check if there are 2 or more 'A'
        if count_A >= 2:
            return False  # Return False if the condition is met
        
        return True  # Return True if neither condition is met
        

