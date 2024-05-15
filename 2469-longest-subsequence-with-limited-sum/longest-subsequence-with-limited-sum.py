class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        
        # Sort the nums list to consider the smallest elements first for each query
        nums.sort()
        
        # Initialize the list to store results for each query
        list1 = []
        
        # Iterate over each query in queries
        for i in queries: 
            
            countt = 0  # Initialize count of elements that can be included
            valuee = 0  # Initialize sum of the included elements
            
            # Iterate over each number in sorted nums
            for j in nums:
                # Check if adding the current number keeps the sum within the query limit
                if valuee + j <= i:
                    countt += 1  # Increment the count of included elements
                    valuee += j  # Add the current number to the sum
            
            # Append the result for the current query to the result list
            list1.append(countt)
        
        return list1  # Return the list of results for all queries
