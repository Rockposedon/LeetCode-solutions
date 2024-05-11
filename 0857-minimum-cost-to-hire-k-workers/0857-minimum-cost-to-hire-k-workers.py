import heapq

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        n = len(quality)

        # Sort workers by the wage-to-quality ratio in ascending order
        workers = sorted((wage[i] / quality[i], quality[i]) for i in range(n))

        min_cost = float('inf')  # Initialize minimum cost to infinity
        sum_quality = 0  # Initialize sum of qualities of selected workers
        max_heap = []  # Initialize max heap to track highest qualities

        for ratio, qual in workers:
            heapq.heappush(max_heap, -qual)  # Push negated quality to simulate a max heap
            sum_quality += qual  # Add current worker's quality to sum

            if len(max_heap) > k:
                sum_quality += heapq.heappop(max_heap)  # Remove the highest quality worker

            if len(max_heap) == k:
                # Calculate cost based on current worker's ratio and sum of qualities
                min_cost = min(min_cost, sum_quality * ratio)

        return min_cost
