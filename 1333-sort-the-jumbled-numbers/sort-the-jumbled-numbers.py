class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        
        def map_number(num, mapping):
        
            # Convert the number to a string to access each digit
            num_str = str(num)
            # Replace each digit with its corresponding mapping
            mapped_str = ''.join(str(mapping[int(digit)]) for digit in num_str)
            # Convert back to an integer for comparison
            return int(mapped_str)
        
        # Create a list of tuples (mapped_value, original_index, original_value)
        mapped_values = [(map_number(num, mapping), index, num) for index, num in enumerate(nums)]
        
        # Sort based on mapped_value and original_index to maintain stability
        mapped_values.sort()
        
        # Extract the original values in the sorted order
        sorted_nums = [num for _, _, num in mapped_values]
        
        return sorted_nums