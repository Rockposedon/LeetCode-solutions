class Solution:
    def findContentChildren(self, g, s):
        # Sort the lists in ascending order
        g.sort()  # Greed factors of children
        s.sort()  # Sizes of available cookies
        
        # Initialize variables
        index = 0  # Index for iterating through sizes of available cookies
        cnt = 0    # Counter for counting content children
        
        # Iterate through both lists
        while index < len(s) and cnt < len(g):
            # If the size of the current cookie is sufficient for the current child's greed
            if s[index] >= g[cnt]:
                cnt += 1  # Increment the count of content children
            index += 1  # Move to the next available cookie
            
        # Return the count of content children
        return cnt
