# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        if not preorder :
            return None
        left = []
        right = []
        root = TreeNode(preorder[0])
        
        for i in range(1,len(preorder)):
            
            # Left subtree
            if preorder[i] < root.val:
                left.append(preorder[i])
            elif preorder[i] > root.val:
                right.append(preorder[i])
            
        root.left = self.bstFromPreorder(left)
        root.right = self.bstFromPreorder(right)
        
        return root
