# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if root is None:
            return result
        
        q = Queue()
        q.put(root)
        
        while not q.empty():
            level_size = q.qsize()  # Number of nodes at the current level
            current_level = []
            
            for _ in range(level_size):
                node = q.get()
                current_level.append(node.val)
                if node.left is not None:
                    q.put(node.left)
                if node.right is not None:
                    q.put(node.right)
            
            result.append(current_level)
        
        return result