# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        # Helper function for depth-first search (dfs)
        def dfs(root):
            
            # Base case: if the node is None, return an empty list
            if not root:
                return []
            
            # If the current node is a leaf, return a list containing the leaf value
            if not root.left and not root.right:
                return [root.val]
            
            # Recursively traverse the left and right subtrees
            return dfs(root.left) + dfs(root.right)
        
        # Check if the leaf values of both trees are equal
        return dfs(root1) == dfs(root2)
