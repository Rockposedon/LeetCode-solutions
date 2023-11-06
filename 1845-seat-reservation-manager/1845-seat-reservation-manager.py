import heapq  # Import the heapq module for heap operations

class SeatManager:
    def __init__(self, n: int):
        # Initialize the SeatManager with 'n' seats
        # Create a list 'unres' containing seat numbers from 1 to 'n'
        self.unres = [i for i in range(1, n + 1)]

    def reserve(self) -> int:
        # Reserve and return the smallest available seat number
        # This is achieved by using a min heap
        # heapq.heappop removes and returns the smallest element from the heap
        return heapq.heappop(self.unres)

    def unreserve(self, seatNumber: int) -> None:
        # Add a seat number back to the available seats
        # This is done by using heapq.heappush to maintain the min heap property
        heapq.heappush(self.unres, seatNumber)

# The SeatManager class is designed to manage seat reservations by maintaining a heap of available seat numbers.
# When you reserve a seat, it provides you with the smallest available seat number, and when a seat is unreserved,
# it adds the seat number back to the available seats heap.

