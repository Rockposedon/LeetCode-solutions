class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        
        # Create a dictionary to map each stop to the set of routes that pass through it
        stop_to_routes = defaultdict(set)
        for i, route in enumerate(routes):
            for stop in route:
                stop_to_routes[stop].add(i)
        
        # Initialize a deque for BFS and a set to keep track of visited stops
        queue = deque([(source, 0)])
        visited = set([source])
        
        # Perform BFS
        while queue:
            current_stop, buses = queue.popleft()
            
            # Check if the target stop is reached
            if current_stop == target:
                return buses
            
            # Explore routes passing through the current stop
            for route_index in stop_to_routes[current_stop]:
                for next_stop in routes[route_index]:
                    if next_stop not in visited:
                        visited.add(next_stop)
                        queue.append((next_stop, buses + 1))
                
                # Mark the route as visited to avoid revisiting
                routes[route_index] = []  
            
        # If no path is found
        return -1