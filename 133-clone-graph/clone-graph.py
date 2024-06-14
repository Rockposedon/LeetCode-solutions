"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node :
            return node
        OldtoNew = {}
        def dfs(node):
            if node in OldtoNew:
                return OldtoNew[node]
            else:
                copy = Node(node.val)
                OldtoNew[node] = copy
                for neg in node.neighbors:
                    copy.neighbors.append(dfs(neg))
                return copy
        return dfs(node)