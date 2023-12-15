class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        # Iterate through each pair of cities in the given paths
        for i in range(len(paths)):
            candidate = paths[i][1]  # Consider the second city in the current path as a candidate destination
            good = True  # Assume the current candidate is a good destination
            
            # Check if the current candidate is the starting city of any other path
            for j in range(len(paths)):
                if paths[j][0] == candidate:
                    good = False  # If the candidate is a starting city, mark it as not a good destination
                    break
            
            # If the candidate is a good destination, return it
            if good:
                return candidate
        
        # If no good destination is found, return an empty string
        return ""