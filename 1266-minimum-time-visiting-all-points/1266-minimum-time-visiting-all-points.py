class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        # Initialize the total time
        time = 0  

        # Iterate through each pair of consecutive points
        for i in range(1, len(points)):
            
            # Calculate the time to move from the current point to the next point
            time += max(
                abs(points[i][0] - points[i - 1][0]),
                abs(points[i][1] - points[i - 1][1])
            )

        # Return the total time to visit all points
        return time  