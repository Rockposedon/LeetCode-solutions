# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # If array is empty, return None
        if not nums:
            return None
        
        # Find the middle element 
        mid = len(nums) // 2
        
        # Create a new root TreeNode with the middle element as the value
        root = TreeNode(nums[mid])
        
        # Recursively create the left subtree with the elements before the middle element
        root.left = self.sortedArrayToBST(nums[:mid])
        
        # Recursively create the right subtree with the elements after the middle element
        root.right = self.sortedArrayToBST(nums[mid+1:])
        
        # Return the root of the constructed BST
        return root
"""
    def insert(self,data):
        if self.val is None:
            self.val = data
        if self.val > data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = TreeNode(data)
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right = TreeNode(data)
"""
                



