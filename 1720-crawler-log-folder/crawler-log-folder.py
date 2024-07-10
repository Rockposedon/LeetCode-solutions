class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []  # Stack to track directory levels
        
        for i in logs:
            
            if i == "./":
                continue  # Stay in the current directory
            elif i == "../":
                if stack:
                    stack.pop()  # Go up one directory level if possible
            else:
                stack.append(i)  # Move into a subdirectory
        
        return len(stack)  # Return the number of operations needed
