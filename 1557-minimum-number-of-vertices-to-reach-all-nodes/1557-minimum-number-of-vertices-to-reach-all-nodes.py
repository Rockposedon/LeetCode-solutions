class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # Initialize a list to keep track of nodes that have incoming edges
        parent = [False] * n
        
        # Mark nodes that have incoming edges
        for u, v in edges:
            parent[v] = True
        
        # Collect nodes that have no incoming edges
        ans = []
        for u in range(n):
            if not parent[u]:
                ans.append(u)
        
        return ans