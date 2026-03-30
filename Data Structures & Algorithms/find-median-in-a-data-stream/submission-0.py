from heapq import heappush, heappop
class MedianFinder:

    def __init__(self):
        self.max = []
        self.min = []

    def addNum(self, num: int) -> None:
        if len(self.min) > 0 and num > self.min[0]:
            heappush(self.min, num)
        else:
            heappush(self.max, -num)
        
        if len(self.min) > len(self.max)+1:
            heappush(self.max, -heappop(self.min))
        elif len(self.max) > len(self.min) + 1:
            heappush(self.min, -heappop(self.max))

    def findMedian(self) -> float:
        if len(self.min) == len(self.max):
            return (self.min[0] + -(self.max[0]))/2
        elif len(self.min) > len(self.max):
            return self.min[0]
        else:
            return -self.max[0]
            
        