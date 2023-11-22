class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        
        # Dictionary to store elements grouped by their diagonal sums
        dic = {}

        # Iterate through each row in the 2D array
        for i in range(len(nums)):
            
            # Iterate through each element in the row
            for j in range(len(nums[i])):
            
                # Calculate the diagonal sum
                diagonal_sum = i + j

                # Check if the diagonal sum already exists in the dictionary
                if dic.get(diagonal_sum, 0):
                    # If yes, insert the current element at the beginning of the list
                    dic[diagonal_sum].insert(0, nums[i][j])
                else:
                    # If no, create a new list with the current element
                    dic[diagonal_sum] = [nums[i][j]]

        # List to store the final result in diagonal order
        ans = []

        # Iterate through the keys of the dictionary
        for i in dic:
            # Extend the result list with the elements from the corresponding list
            ans.extend(dic[i])

        # Return the final result
        return ans