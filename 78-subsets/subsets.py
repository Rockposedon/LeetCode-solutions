class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        # Helper function to generate subsets recursively
        def recursive(start, path):
            
            # Append the current subset (path) to the result
            result.append(path)
            
            # Iterate over the possible next elements to add to the subset
            for i in range(start, len(nums)):
                # Recursively call with the next starting index and the new path including nums[i]
                recursive(i + 1, path + [nums[i]])
        
        # Initialize the result list to store all subsets
        result = []
        # Start the recursion with an empty path
        recursive(0, [])
        # Return the final list of subsets
        return result