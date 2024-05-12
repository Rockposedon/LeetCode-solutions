class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # List to store scores
        scores = []
        
        for i in operations:
            
            # If operation is '+', add the last two valid scores
            if i == "+":  
                scores.append(scores[-1] + scores[-2])
            
            # If operation is 'D', double the last valid score
            elif i == "D":  
                scores.append(scores[-1] * 2)
            
            # If operation is 'C', remove the last valid score
            elif i == "C":  
                scores.pop()
            
            # If operation is an integer, add it as a valid score
            else:  
                scores.append(int(i))
                
        # Return the sum of all valid scores
        return sum(scores)  
