class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        
        """
        Initialize the KthLargest class with a given integer k and a list of integers nums.
        This class maintains the kth largest element in a stream of numbers.
        """
        
        self.k = k
        
        # Min-heap to store the kth largest elements
        self.heap = []  
        for i in nums:
            
            # Add initial elements to the heap
            self.add(i) 
            
    def add(self, val: int) -> int:
        
        """
        Add a new value to the stream and return the kth largest element.
        """
        
        # Push the new value onto the heap
        heapq.heappush(self.heap, val)
        
        # If the heap exceeds size k
        if len(self.heap) > self.k:  
            
            # Remove the smallest element to maintain the heap size
            heapq.heappop(self.heap)  
            
        # The root of the heap is the kth largest element
        return self.heap[0]  

# Example usage:
# kthLargest = KthLargest(3, [4, 5, 8, 2])
# print(kthLargest.add(3))  # Output: 4
# print(kthLargest.add(5))  # Output: 5
# print(kthLargest.add(10)) # Output: 5
# print(kthLargest.add(9))  # Output: 8
# print(kthLargest.add(4))  # Output: 8

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)