class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        
        for i in s:
            
            # Push the current character onto the stack
            stack.append(i)  
            
            # Check if the last three characters form the sequence "abc"
            if len(stack) >= 3 and stack[-1] == "c" and stack[-2] == "b" and stack[-3] == "a":
                
                # Pop the last three characters if they form "abc"
                stack.pop()
                stack.pop()
                stack.pop()
                
        # If the stack is empty, the string is valid
        return len(stack) == 0
