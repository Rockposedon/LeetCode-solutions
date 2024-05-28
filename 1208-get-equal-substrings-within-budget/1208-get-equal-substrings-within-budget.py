class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        
        # Calculate the cost for changing each character
        costs = [abs(ord(sc) - ord(tc)) for sc, tc in zip(s, t)]
        
        # Initialize variables for the sliding window
        start = 0
        current_cost = 0
        max_length = 0
        
        # Iterate over the costs using a sliding window approach
        for end in range(len(costs)):
            current_cost += costs[end]
            
            # If the current cost exceeds maxCost, shrink the window from the start
            while current_cost > maxCost:
                current_cost -= costs[start]
                start += 1
            
            # Update the maximum length of the substring
            max_length = max(max_length, end - start + 1)
        
        return max_length