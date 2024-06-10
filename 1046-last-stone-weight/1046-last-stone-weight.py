class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        # Sort the stones in descending order
        stones.sort(reverse=True)
        
        while len(stones) > 1:
            # Take the two largest stones
            first = stones.pop(0)
            second = stones.pop(0)
            
            # If they are not the same, push the difference back into the list and sort again
            if first != second:
                new_stone = abs(first - second)
                stones.append(new_stone)
                stones.sort(reverse=True)
        
        # Return the last remaining stone or 0 if there are no stones left
        return stones[0] if stones else 0