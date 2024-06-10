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

