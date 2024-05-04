class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        """
        Calculate the minimum number of boats required to carry all people based on weight limit.

        Args:
            people (List[int]): List of weights of people.
            limit (int): Maximum weight limit per boat.

        Returns:
            int: Minimum number of boats required.
        """
        n = len(people)
        people.sort()  # Sort the people by weight
        
        left = 0  # Pointer for the lightest person
        right = n - 1  # Pointer for the heaviest person
        
        boats = 0  # Initialize boat count
        
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1  # Both can fit in one boat
            right -= 1  # The heaviest person boards the boat
            boats += 1  # Increment boat count
        
        return boats