class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # Initialize an empty dictionary to store element frequencies
        dict1 = {}

        # Count occurrences of each element in the list
        for i in arr:
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1

        # Create a set to store unique counts
        freq = set()

        # Check whether the counts are unique
        for i in dict1:
            if dict1[i] in freq:
                return False
            freq.add(dict1[i])

        # If all counts are unique, return True
        return True
