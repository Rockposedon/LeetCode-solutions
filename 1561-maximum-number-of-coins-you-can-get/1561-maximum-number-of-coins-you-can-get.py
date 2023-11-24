class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        result_of_mine = 0
        n = len(piles)

        """Time Limit Exceeded"""
        # Soting piles using Bubble Sort
        # for i in range(n):
        #     for j in range(0, n-i-1):
        #         if piles[j] > piles[j+1]:
        #             # Swap elements if they are in the wrong order
        #             piles[j], piles[j+1] = piles[j+1], piles[j]
        
        """Sort Function to over come time limit error"""
        def sort(arr):
            
            # Base case: if the array has 0 or 1 elements, it is already sorted
            if len(arr) <= 1:
                return arr
            
            else:
                # Choose the pivot as the first element of the array
                pivot = arr[0]

                # Create a list of elements less than or equal to the pivot
                less = [x for x in arr[1:] if x <= pivot]

                # Create a list of elements greater than the pivot
                greater = [x for x in arr[1:] if x > pivot]

                # Recursively sort the "less" and "greater" subarrays
                return sort(less) + [pivot] + sort(greater)
        
        piles=sort(piles)

                    
        #  every third pile starting from the end
        for i in range(n // 3,n, 2):
            # Add the coins from every alternate pile to the total
            result_of_mine += piles[i]

        return result_of_mine

        