class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        n = len(arr)
        
        # Sort the array in ascending order
        arr.sort()
        
        # Set the first element to 1
        arr[0] = 1
        
        # Iterate through the array starting from the second element
        for i in range(1, n):
            # Ensure that the current element is at most 1 greater than the previous element
            arr[i] = min(arr[i], arr[i - 1] + 1)
        
        # Return the maximum element in the modified array
        return arr[n - 1]
