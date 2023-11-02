# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
	    count = 0

	    def check(root):
		    nonlocal count
		    if root:
			    check(root.left)
			    check(root.right)

			    root.total, root.nodes = root.val, 1

			    if root.left:
				    root.total += root.left.total
				    root.nodes += root.left.nodes

			    if root.right:
				    root.total += root.right.total
				    root.nodes += root.right.nodes

			    if root.val == int(root.total / root.nodes):
				    count += 1

	    check(root)

	    return count