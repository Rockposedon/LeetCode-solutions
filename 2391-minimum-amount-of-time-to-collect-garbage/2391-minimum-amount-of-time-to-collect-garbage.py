class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        
        # Initialize variables to store the indices of M, G, and P in the garbage list
        m = 0
        g = 0
        p = 0
        
        # Variable to store total time to collect garbage
        totaltime = 0

        # Iterate through each element in the garbage list
        # Here "i" is the index of string of an list
        for i in range(len(garbage)):
            
            # Check if "M" is in the current element
            if "M" in garbage[i]:
                m = i
            # Check if "P" is in the current element
            if "P" in garbage[i]:
                p = i
            # Check if "G" is in the current element
            if "G" in garbage[i]:
                g = i

            # Add the time it takes to clean the current garbage element to the total time
            totaltime += len(garbage[i])

        # Add the time it takes to travel to each garbage location before cleaning
        totaltime += sum(travel[:m])  # Travel time to M
        totaltime += sum(travel[:g])  # Travel time to G
        totaltime += sum(travel[:p])  # Travel time to P

        # Return the total time needed for garbage collection and travel
        return totaltime
