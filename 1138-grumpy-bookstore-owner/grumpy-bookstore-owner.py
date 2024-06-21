class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        happy = 0
        n = len(customers)

        for i in range(n):
            if grumpy[i] == 0:
                happy += customers[i]
        

        extra = 0
        for i in range(minutes):
            if grumpy[i] == 1:
                extra += customers[i]
        
        maxExtra = extra
        
        # Sliding window to find the maximum extra satisfied customers
        for i in range(minutes, n):
            if grumpy[i - minutes] == 1:
                extra -= customers[i - minutes]
            if grumpy[i] == 1:
                extra += customers[i]
            
            maxExtra = max(maxExtra, extra)
        
        return happy + maxExtra