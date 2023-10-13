class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Get the number of steps in the cost list
        n = len(cost)
        
        # Initialize variables to keep track of the minimum cost
        # when taking 0 or 1 steps respectively.
        prev2 = cost[0]  # Minimum cost for taking 0 steps (starting point)
        prev1 = cost[1]  # Minimum cost for taking 1 step
        
        # Loop through the cost list starting from the 2nd step (index 2)
        for i in range(2, n):
            # Calculate the minimum cost to reach the current step (i)
            # by taking either one step from prev1 or two steps from prev2
            temp = cost[i] + min(prev1, prev2)
            
            # Update prev2 and prev1 for the next iteration
            prev2 = prev1
            prev1 = temp
        
        # The minimum cost to reach the top (n-1) step is the minimum
        # between the cost of taking the last step and the cost of taking
        # the second-to-last step.
        return min(prev1, prev2)
