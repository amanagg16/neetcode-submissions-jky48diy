from heapq import heappush, heappop
class MedianFinder:

    def __init__(self):
        self.max_lower = [] # max heap for the first part
        self.min_higher = [] # min heap for the second part

    def addNum(self, num: int) -> None:
        if self.max_lower and num <= -self.max_lower[0]:
           heappush(self.max_lower, -num)
        else:
            heappush(self.min_higher, num)
        
        if len(self.min_higher) > len(self.max_lower) + 1:
            heappush(self.max_lower, -heappop(self.min_higher))
        elif len(self.max_lower) > len(self.min_higher) + 1:
            heappush(self.min_higher, -heappop(self.max_lower))

    def findMedian(self) -> float:
        if len(self.max_lower) > len(self.min_higher):
            return -self.max_lower[0]
        elif len(self.max_lower) < len(self.min_higher):
            return self.min_higher[0]
        elif len(self.max_lower) == len(self.min_higher):
            return (-self.max_lower[0] + self.min_higher[0])/2