class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        data = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
                }
        
        if not digits:
            return []
        # Declaring empty list of string as a starting point 
        final_c = ['']
        # Iterate through each element in digits
        for i in digits:
            # Declaring another list to
            updating_c = []
            # Iterate through each letter of dictionary data
            for j in data[i]:
                # Iterate in fina_c and append the current letter
                for k in final_c:
                    updating_c.append(k+j)
            # update final list of combinations
            final_c = updating_c
            
        return final_c
    
    