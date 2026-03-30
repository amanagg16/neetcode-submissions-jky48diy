from collections import Counter
from heapq import heappush, heappop
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        heap = []

        for num, freq in c.items():
            heappush(heap, (freq, num)) # basically this tuple will follow heap property on the basis of first element...
            if len(heap) > k:
                heappop(heap)
        

        res = [freq_num[1] for freq_num in heap]
        return res