"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        result = []
        
        def traverse(root):
            if not root:
                return
            result.append(root.val)
            for node in root.children:
                traverse(node)
        
        traverse(root)
        return result