class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        
        alice_plays = 0
        bob_plays = 0
        count = 1 
        
        # Iterate through the colors string starting from the second character.
        for i in range(1, len(colors)):
            
            # If the current color is the same as the previous one, increase the count.
            if colors[i] == colors[i - 1]:
                count += 1
            else:
                
                # If the color changed, check the previous player and update their plays.
                if colors[i - 1] == 'A':
                    
                    # Alice's turn: Add the number of consecutive plays minus 2 (if it's positive).
                    alice_plays += max(0, count - 2)
                else:
                    
                    # Bob's turn: Add the number of consecutive plays minus 2 (if it's positive).
                    bob_plays += max(0, count - 2)
                    
                # Reset the count for consecutive plays.
                count = 1
        
        # After the loop, check the last color to update the final plays.
        if colors[-1] == 'A':
            
            alice_plays += max(0, count - 2)
        else:
            
            bob_plays += max(0, count - 2)
        
        # Compare Alice and Bob's total plays and return True if Alice played more.
        return alice_plays > bob_plays
