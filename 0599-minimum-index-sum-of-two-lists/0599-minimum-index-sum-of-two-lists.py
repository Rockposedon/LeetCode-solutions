class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        # Create an empty dictionary to store the sum of indices for each restaurant
        dictA = {}
        # Create an empty list to store the sums of indices
        listA = []
        
        # Iterate over the indices of list1
        for i in range(len(list1)):
            
            # Iterate over the indices of list2
            for j in range(len(list2)):
                
                # Check if the current restaurant is in both lists
                if list1[i] == list2[j]:
                    
                    # Calculate the sum of the indices
                    sum_ij = i+j
                    
                    # Add the sum to the list of sums
                    listA.append(sum_ij)
                    
                    # Add the restaurant and its sum to the dictionary
                    dictA[list1[i]] = sum_ij
        
        # Find the minimum sum of indices
        p = min(listA)
        
        # Create an empty list to store the result
        result = []
        
        # Iterate over the items in the dictionary
        for key, value in dictA.items():
            
            # Check if the sum of indices is equal to the minimum sum
            if value == p:
                
                # Add the restaurant to the result list
                result.append(key)
                
        # Return the list of restaurants with the minimum sum of indices
        return result