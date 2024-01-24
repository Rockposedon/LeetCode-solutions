# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        ans=0
        def dfs(node, p):
            nonlocal ans
            if not node: return
            x=node.val
            p^=(1<<x)
            if (not node.left) and (not node.right):
                if p.bit_count()<=1: ans+=1
                return
            dfs(node.left, p)
            dfs(node.right, p)
        p=0
        dfs(root, p)
        return ans