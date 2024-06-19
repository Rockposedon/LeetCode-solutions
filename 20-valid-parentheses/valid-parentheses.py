# Approach 1st
"""
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
"""

# Approach 2nd
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        rev_pair = {')': '(', '}': '{', ']': '['}
        for c in s:
            if c in rev_pair:
                # If the stack is not empty and the top element of the stack is the matching opening parenthesis
                if stack and stack[-1] == rev_pair[c]:
                    stack.pop()  # Pop the top element from the stack
                else:
                    return False  # If the top element is not the matching opening parenthesis, return False
            else:
                stack.append(c)  # If it's an opening parenthesis, push it onto the stack
        return not stack  # Return True if the stack is empty, meaning all parentheses were matched and closed correctly
