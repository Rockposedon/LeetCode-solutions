class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        
        count = 0
        curr_height = 0
        
        # Iterate through each rung in the given list
        for rung in rungs:
            # If the gap between the current height and the next rung is greater than the allowed distance
            if rung - curr_height > dist:
                # Calculate the number of rungs needed to be added
                count += (rung - curr_height - 1) // dist
            # Update the current height to the height of the current rung
            curr_height = rung
        
        return count

                