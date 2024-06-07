# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = []
        def inOrder(node):
            if node is None:
                return 
            inOrder(node.left)
            result.append(node.val)
            inOrder(node.right)
        inOrder(root)
        print(k)
        return result[k-1]