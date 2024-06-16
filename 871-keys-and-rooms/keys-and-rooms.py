
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # Initialize a list 'seen' with False values to keep track of visited rooms
        seen = [False] * len(rooms)
        
        # Mark the first room (room 0) as visited
        seen[0] = True
        
        # Use a stack to perform a depth-first search (DFS) starting from room 0
        stack = [0]
        
        # Continue the DFS until there are no more rooms to process
        while stack:
            # Pop a room from the stack to visit
            node = stack.pop()
            
            # Iterate through all keys in the current room
            for key in rooms[node]:
                
                # If the room corresponding to the key has not been visited yet
                if not seen[key]:
                    
                    # Mark the room as visited
                    seen[key] = True
                    
                    # Add the room to the stack to visit its keys later
                    stack.append(key)
        
        # Return True if all rooms have been visited (i.e., all elements in 'seen' are True)
        return all(seen)
