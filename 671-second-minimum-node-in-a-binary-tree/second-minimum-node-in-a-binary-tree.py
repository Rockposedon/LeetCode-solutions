# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        # Initialize the smallest and second smallest values to infinity
        self.smallest = float('inf')
        self.second_smallest = float('inf')
        
        def dfs(root):
            # Base case
            if not root:
                return -1
            
            # Update the smallest value if the current node's value is smaller
            if root.val < self.smallest:
                self.smallest = root.val
            
            # Update the second smallest value if the current node's value is 
            # between the smallest and second smallest
            if root.val > self.smallest and root.val < self.second_smallest:
                self.second_smallest = root.val
            
            # Recursively traverse the left and right subtrees
            dfs(root.left)
            dfs(root.right)
        
        # Start the depth-first search traversal from the root
        dfs(root)
        
        # If the second smallest value is still infinity, it means there was no second minimum value
        if self.second_smallest == float('inf'):
            return -1
        
        # Return the second smallest value
        return self.second_smallest
