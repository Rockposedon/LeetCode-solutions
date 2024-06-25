# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        # Initialize the sum of nodes to 0
        self.node_sum = 0
        
        # Function to perform reverse inorder traversal/ 
        # also RDL(process right subtree, then node, then left subtree)
        def reverse_inorder(node):
            if not node:  # Base case: if the node is None, return
                return
            
            # Traverse the right subtree
            reverse_inorder(node.right)  
            
            # Update the running sum
            self.node_sum += node.val 
            # Update the node's value to the running sum
            node.val = self.node_sum  
            
            # Traverse the left subtree
            reverse_inorder(node.left)  
        
        # Start the traversal from the root
        reverse_inorder(root)  
        # Return the modified tree
        return root  
