class Solution:
    def isPathCrossing(self, path: str) -> bool:
        
        # Set to keep track of visited coordinates, starting with the origin (0, 0).
        visited = {(0, 0)}
        
        # Initialize the current coordinates.
        x, y = 0, 0
        
        # Iterate through each direction in the given path.
        for direction in path:
            # Update the coordinates based on the current direction.
            if direction == 'N':
                y += 1
            elif direction == 'E':
                x += 1
            elif direction == 'S':
                y -= 1
            else:  # direction == 'W'
                x -= 1
            
            # Check if the current coordinates have been visited before.
            if (x, y) in visited:
                # If visited, a cycle is detected, and the path is crossing itself.
                return True
            else:
                # If not visited, add the current coordinates to the set of visited locations.
                visited.add((x, y))
        
        # If no cycle is detected after processing the entire path, the path does not cross itself.
        return False
