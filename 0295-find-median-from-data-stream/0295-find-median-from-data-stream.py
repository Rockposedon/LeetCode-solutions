# 1st approach
'''
from sortedcontainers import SortedList
import statistics

class MedianFinder:

    def __init__(self):
        self.list = SortedList()

    def addNum(self, num: int) -> None:
        self.list.add(num)

    def findMedian(self) -> float:
        return statistics.median(self.list)
'''
# 2nd approach
import heapq

class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        if len(self.small) == len(self.large):
            heapq.heappush(self.large, -heapq.heappushpop(self.small, -num))
        else:
            heapq.heappush(self.small, -heapq.heappushpop(self.large, num))

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return (self.large[0] - self.small[0]) / 2.0
        else:
            return float(self.large[0])