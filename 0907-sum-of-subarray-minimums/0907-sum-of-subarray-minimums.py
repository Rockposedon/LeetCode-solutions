''' 
    First Approach 
    
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:

        # Length of main array
        n = len(arr)
        

        # Taking variable to store sum of Sub Arrays
        result = 0

        # Iterate through each element in the array
        for i in range(n):
            
            # Initialize the minimum element as the current element
            min_element = arr[i]

            # Iterate through subarrays starting from the current element
            for j in range(i, n):
                
                # Update the minimum element in the current subarray
                min_element = min(min_element, arr[j])

                # Add the minimum element to the result for each subarray
                result += min_element

        # Return the final sum of minimum elements in all subarrays
        return result % (10**9 + 7)
    '''
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        
        # Define the modulo value as specified in the problem
        mod = 10**9 + 7
        # Initialize an empty stack to keep track of indices
        stack = []
        # Initialize the result variable to store the final sum
        result = 0

        # Loop through the array elements along with their indices
        for i, num in enumerate(arr):
            
            # Process elements in the stack while the current element is less than the element at the top of the stack
            while stack and num < arr[stack[-1]]:
                
                # Pop the top element from the stack
                j = stack.pop()
                # Calculate the contribution of the popped element to the result
                # The contribution is the product of the element value, the width of the subarray (i - j),
                # and the height of the subarray (j - k), where k is the previous element in the stack
                k = stack[-1] if stack else -1
                result += arr[j] * (i - j) * (j - k)

            # Push the current index onto the stack
            stack.append(i)

        # Process any remaining elements in the stack
        while stack:
            
            # Pop the top element from the stack
            j = stack.pop()
            # Calculate the contribution of the popped element to the result
            # Similar to the previous calculation, but using len(arr) as the width of the subarray
            k = stack[-1] if stack else -1
            result += arr[j] * (len(arr) - j) * (j - k)

        # Return the final result modulo the specified value
        return result % mod