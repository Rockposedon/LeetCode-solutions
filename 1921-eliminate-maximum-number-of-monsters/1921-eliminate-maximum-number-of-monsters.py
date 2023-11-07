class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        
        # when both lists are empty (base case)
        if not dist or not speed:
            return 0
        
        n = len(dist)
        
        # Initialize list element with 0 of size n
        time = [0] * n
        
        for i in range(n):
            
            # Calculating time for each monster to reach the city 
            time[i] = dist[i] / speed[i]

        # # Bubble sort to sort time list 
        # for i in range(n):
        #     for j in range(0, n - i - 1):
        #         if time[j] > time[j + 1]:
        #             time[j], time[j + 1] = time[j + 1], time[j]
        time.sort()
        # Initialize a count variable to track monsters that arrive on time.
        count =      0

        # Loop through the sorted 'time' list.
        for i in range(len(time)):
            
            # Check if the time taken by a monster is less than or equal to its position in the sorted list
            if time[i] <= i:
                
                break   # Stop counting when the monster reaches the city
            count += 1  # If monster not reaches the city increment the count

        # The maximumu number of monster that eliminated
        return count
