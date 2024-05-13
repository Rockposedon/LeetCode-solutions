class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack1 = []
        
        for i in logs:
            if i == "./":
                continue
            elif i == "../":
                if stack1:
                    stack1.pop()
            else:
                stack1.append(i)
        return len(stack1)