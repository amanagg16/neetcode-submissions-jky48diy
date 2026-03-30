from heapq import heappush, heappop
from typing import List
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [] # max heap

        for x,y in points:
            distance = pow(x,2) + pow(y,2)
            heappush(heap, (-distance,[x,y]))
            while len(heap) > k:
                heappop(heap)

        return [point[1] for point in heap]