# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        # This list will hold the nodes values in sorted order
        sorted_arr = []
        
        # Helper function to perform in-order traversal
        def Inorder(node):
            if not node:
                return None
            
            Inorder(node.left)  # Traverse the left subtree
            sorted_arr.append(node.val)  # Visit the node
            Inorder(node.right)  # Traverse the right subtree
            
        # Populate the sorted_arr list with in-order traversal of the BST
        Inorder(root)
        
        # Helper function to construct a balanced BST from sorted array
        def Balance(left, right):
            
            if left > right:
                return None  
            
            mid = (left + right) // 2  # Find the middle element
            root = TreeNode(sorted_arr[mid])  # Create a new tree node
            
            # Recursively construct the left and right subtrees
            root.left = Balance(left, mid - 1)  # Left subtree
            root.right = Balance(mid + 1, right)  # Right subtree
            
            return root  # Return the root of the balanced subtree
        
        # Construct the balanced BST and return its root
        return Balance(0, len(sorted_arr) - 1)
