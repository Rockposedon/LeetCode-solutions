class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        # Initialize a frequency array to keep track of the occurrences of each element
        freq = [0] * (len(nums) + 1)
        
        # Initialize an empty list to store the final result as a matrix
        ans = []

        # Iterate through each element in the input list nums
        for c in nums:
            # Check if the frequency of the current element is greater than or equal to the length of the result list
            if freq[c] >= len(ans):
                # If true, add a new empty list to the result list, representing a new row in the matrix
                ans.append([])

            # Append the current element to the list at index freq[c] in the result list
            ans[freq[c]].append(c)
            
            # Increment the frequency of the current element
            freq[c] += 1

        # Return the final result, which is a matrix represented by the list of lists ans
        return ans
