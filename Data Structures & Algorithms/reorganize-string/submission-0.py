from heapq import heapify, heappush, heappop
from collections import Counter
class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        maxheap = []
        max_freq = 0
        for char, freq in counter.items():
            maxheap.append([-freq, char])
            max_freq = max(max_freq, freq)
        
        if max_freq > (len(s)+1)//2:
            return ''
        heapify(maxheap)
        res = ''
        prev = None
        while maxheap or prev:

            freq, char = heappop(maxheap)
            res += char
            freq += 1

            if prev:
                heappush(maxheap, prev)
                prev = None

            if freq!=0:
                prev = [freq, char]
            
        return res