from sortedcontainers import SortedList
import statistics

class MedianFinder:

    def __init__(self):
        self.list = SortedList()

    def addNum(self, num: int) -> None:
        self.list.add(num)

    def findMedian(self) -> float:
        return statistics.median(self.list)