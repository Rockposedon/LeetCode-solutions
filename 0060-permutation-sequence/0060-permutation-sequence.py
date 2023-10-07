class Solution:
    def getPermutation(self,n, k):
    # Create a list of numbers from 1 to n
        nums = list(range(1, n + 1))
    
        # list to store result
        result = []

        # Decrement k to make it zero-based
        k -= 1

        for i in range(n):
            # Calculate the index of the current digit in nums
            # This index determines which number to choose for the current position
            index = k // math.factorial(n - 1 - i)
        
            # Append the selected digit to the result
            result.append(nums[index])

            # Update k to the remainder after choosing the digit
            k %= math.factorial(n - 1 - i)

            # Remove the chosen digit from the remaining options
            nums.pop(index)

        # Convert the result list into a string and return it
        return ''.join(map(str, result))