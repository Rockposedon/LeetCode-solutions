class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # Initialize an empty dictionary to store groups of anagrams
        anagrams = {}

        # Initialize an empty list to store the final result
        result = []

        # Iterate through each word in the input list
        for word in strs:

            # Sort the characters of the word to create a unique representation
            sorted_str = "".join(sorted(word))

            # Check if the sorted string is already present in the dictionary
            if sorted_str not in anagrams:

                # If not present, create a new list with the word as the only element
                anagrams[sorted_str] = [word]

            else:

                # If present, append the word to the list of anagrams
                anagrams[sorted_str].append(word)

        # Iterate through the dictionary and append the values (lists of anagrams) to the result
        for key in anagrams:
            result.append(anagrams[key])

        # Return the final result
        return result