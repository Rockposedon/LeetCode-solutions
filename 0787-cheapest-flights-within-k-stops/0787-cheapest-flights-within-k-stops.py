class Solution:
    def findCheapestPrice(self, n: int, grid: List[List[int]], src: int, dst: int, k: int) -> int:
        #constructing adjacency matrix
        adj=[[]for i in range(n)]
        for i in grid:
            adj[i[0]].append([i[1],i[2]])
        dist=[float('inf')for i in range(n)]
        dist[src]=0
        q=[[0,src,0]]   #[stops, node, toatlcost]
        while q:
            stp,node,cost=q.pop(0)  #popping from left, alternatively u you can use dequeu()
            if stp>k:
                continue
            for elm in adj[node]:
                adjnode,fcost=elm[0],elm[1]
                if dist[adjnode]>cost+fcost and stp<=k:  # <= check means we are taking into considerating all the stops, bcz we are not including the staring and the ending stops
                    dist[adjnode]=cost+fcost
                    q.append([stp+1,adjnode,cost+fcost])   #increasing one stop
        if dist[dst]==float('inf'):
            return -1
        return dist[dst]
