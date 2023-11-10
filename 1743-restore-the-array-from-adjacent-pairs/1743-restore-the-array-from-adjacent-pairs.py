class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        
    
        # Create an adjacency dictionary to store the neighbors of each element
        adjacency_dict = {}

        # Populate the adjacency dictionary based on the given adjacentPairs
        for arr in adjacentPairs:
            if arr[0] in adjacency_dict:
                adjacency_dict[arr[0]].append(arr[1])
            else:
                adjacency_dict[arr[0]] = [arr[1]]
            
            if arr[1] in adjacency_dict:
                adjacency_dict[arr[1]].append(arr[0])
            else:
                adjacency_dict[arr[1]] = [arr[0]]

        # Find the starting point (element with only one neighbor)
        smallest_key = None
        for key in adjacency_dict:
            if len(adjacency_dict[key]) == 1:    
                smallest_key = key
                break

        # Initialize the result array with the starting point
        nums = [smallest_key]

        # Use a set to keep track of visited elements
        visited = set(nums)

        # Reconstruct the array until it reaches the desired length
        while len(nums) < len(adjacentPairs) + 1:
            current = nums[-1]
            next_candidates = adjacency_dict[current]

            # Iterate through the neighbors of the current element
            for candidate in next_candidates:
                if candidate not in visited:
                    # Add the candidate to the result array
                    nums.append(candidate)
                    # Mark the candidate as visited
                    visited.add(candidate)
                    # Break to move to the next iteration of the while loop
                    break

        # Return the reconstructed array
        return nums

        