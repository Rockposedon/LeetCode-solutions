class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        
        # Initialize frequency array to store degree of each node
        freq = [0] * n
        
        # Count degree of each node
        for a, b in roads:
            freq[a] += 1  # increment degree of node a
            freq[b] += 1  # increment degree of node b
        
        # Sort frequency array in ascending order
        freq.sort()
        
        # Initialize result variable to store maximum importance
        result = 0
        
        # Calculate maximum importance
        for i in range(n):
            # Add product of frequency and its 1-based index to result
            result += (i + 1) * freq[i]
        
        # Return maximum importance
        return result