from heapq import heappush, heappop, heapify
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = [] # of size k
        self.k = k
        self.nums = nums
        for n in self.nums:
            heappush(self.heap, n)
            if len(self.heap) > k:
                heappop(self.heap)
        

    def add(self, val: int) -> int:
        heappush(self.heap, val)
        while len(self.heap) > self.k:
            heappop(self.heap)
        return self.heap[0]
