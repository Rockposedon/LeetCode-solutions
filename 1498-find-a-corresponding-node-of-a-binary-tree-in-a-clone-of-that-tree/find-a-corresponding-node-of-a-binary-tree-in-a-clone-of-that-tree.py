# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        return self.search(cloned, target)
    def search(self, tree: TreeNode, target: TreeNode) -> TreeNode:
        if tree.val == target.val:
            return tree
        if tree.left:
            left = self.search(tree.left,target)
            if left:
                return left
        if tree.right:
            right = self.search(tree.right,target)
            if right:
                return right
            