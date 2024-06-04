# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

    
        
class Solution:

    def smallestDescendant(self, root):
        """
        Find the smallest node in the tree.
        """
        while root.left:
            root = root.left
        return root

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """
        Delete a node with the given key from the tree.
        """
        if not root:
            """
            If the tree is empty, return None.
            """
            return None
        else:
            # if key is smaller then go to left subtree
            if key < root.val:
                root.left = self.deleteNode(root.left, key)
            # if key is greater then go to right subtree
            elif key > root.val:
                root.right = self.deleteNode(root.right, key)
            else:
                # if key is found
                if not root.left:
                    # if left child is None, return right child
                    return root.right
                elif not root.right:
                    # if right child is None, return left child
                    return root.left
                else:
                    # if both children exist
                    temp = self.smallestDescendant(root.right)
                    # replace the value of the current node with the smallest value in the right subtree
                    root.val = temp.val
                    # delete the smallest node in the right subtree
                    root.right = self.deleteNode(root.right, temp.val)

        return root
        
