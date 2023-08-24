class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        H=height
        ans = 0 
        left = 0
        right = len(H) - 1  
        # While the two pointers haven't crossed each other
        while left < right:  
            if H[left] <= H[right]:  # Compare heights at the two pointers
                area = H[left] * (right - left)  # Calculate area using the shorter height
                left += 1  # Move the left pointer towards the center
            else:
                area = H[right] * (right - left)  # Calculate area using the shorter height
                right -= 1  # Move the right pointer towards the center
        
            if area > ans:  # Compare the calculated area with the current maximum area
                ans = area  # Update the maximum area if necessary
    
        return ans  # Return the maximum area
