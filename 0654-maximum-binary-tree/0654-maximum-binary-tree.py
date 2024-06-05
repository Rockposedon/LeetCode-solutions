# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        # Base case: if nums is empty, return None
        if not nums:
            return None
        
        # Find the maximum element in nums to be the root
        rootdata = max(nums)
        
        # Initialize the root node with the maximum value
        root = TreeNode(rootdata)
        
        # Find the index of the maximum element in nums
        idx = nums.index(rootdata)
        
        # Recursively construct the left subtree with the elements before the max element
        root.left = self.constructMaximumBinaryTree(nums[:idx])
        
        # Recursively construct the right subtree with the elements after the max element
        root.right = self.constructMaximumBinaryTree(nums[idx+1:])
        
        return root