class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # Dictionary to map opening brackets to their corresponding closing brackets
        pair = {'(':')','{':'}','[':']'}  
        
        for i in s:
            # If the character is an opening bracket
            if i in pair:  
                # Push the opening bracket onto the stack
                stack.append(i)  
            else:  # If the character is a closing bracket
                   # Check if the stack is not empty and the top of the stack matches 
                if stack and pair[stack[-1]] == i: 
                    
                    # Pop the top element from the stack
                    stack.pop()  
                else:  # If the stack is empty or the top of the stack does not match the closing bracket
                       # The string is not valid, so return False
                    return False  
                
        # If the stack is empty, all brackets were matched correctly, so return True     
        return not stack  