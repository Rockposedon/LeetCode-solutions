class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        # Sort both arrays
        seats.sort()
        students.sort()
        n = len(seats)
        # Initialize the total moves counter
        total_moves = 0
        
        # Calculate the total number of moves required
        for i in range(n):
            total_moves += abs(seats[i] - students[i])
        
        return total_moves
