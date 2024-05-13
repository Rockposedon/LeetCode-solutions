class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # Function to convert time in "HH:MM" format to minutes
        def convert(time):
            h, m = map(int, time.split(':'))
            return h * 60 + m  # Convert time to minutes

        # Convert all time points to minutes and sort them
        minutes = []
        for t in timePoints:
            minutes.append(convert(t))  # Convert each time point and add it to the list
        minutes.sort()  # Sort the list of minutes

        # Initialize min_diff to infinity for comparison
        min_diff = float('inf')

        # Calculate the minimum difference between adjacent time points
        for i in range(len(minutes) - 1):
            diff = minutes[i + 1] - minutes[i]
            min_diff = min(min_diff, diff)  # Update min_diff if a smaller difference is found

        # Calculate the difference between the first and last time points considering the circular nature of time
        diff_between_first_last = minutes[0] + 1440 - minutes[-1]
        min_diff = min(min_diff, diff_between_first_last)  # Update min_diff with the minimum of the two differences

        return min_diff  # Return the minimum time difference found
