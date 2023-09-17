class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        
        # Initialize a queue with the starting position
        queue = [0]
        
        # Create a set to keep track of visited positions
        visited = set([0])
        
        # Initialize a variable to keep track of the maximum reachable position
        mx = 0
        
        while queue:
            node = queue.pop(0)
            
            # If we reached the end, return True
            if node == n - 1:
                return True
            
            # Skip invalid positions
            if node < 0 or node >= n:
                continue
            
            # Explore positions within the jump range
            for i in range(max(mx + 1, node + minJump), min(node + maxJump, n - 1) + 1):
                if s[i] == '0' and i not in visited:
                    queue.append(i)
                    visited.add(i)
            
            # Update the maximum reachable position
            mx = max(mx, node + maxJump)
        
        return False
