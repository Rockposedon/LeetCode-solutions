class Solution:
    def check(self, position, m, mid):
        # Start by placing the first ball
        count = 1 
        # Position of the last placed ball
        prev = position[0] 

        for i in range(1, len(position)):
            # If the current position is at least mid distance from the last ball
            if position[i] - prev >= mid:  
                # Place a new ball
                count += 1  
                # Update the last placed ball position
                prev = position[i]  
                # If we have placed all m balls
                if count >= m:  
                    return True  
        return False  

    def maxDistance(self, position, m):
        position.sort()
        # Minimum possible distance
        low = 0  
        # Maximum possible distance
        high = position[-1] - position[0] 
        # Store the maximum minimum distance
        answer = 0  

        # Binary search
        while high >= low:  
            mid = (low + high) // 2  
            # Check if mid distance is feasible
            if self.check(position, m, mid):  
                answer = mid  
                # Try for a larger distance
                low = mid + 1 
            else:
                # Try for a smaller distance
                high = mid - 1  
        # Return the maximum possible minimum distance
        return answer  
