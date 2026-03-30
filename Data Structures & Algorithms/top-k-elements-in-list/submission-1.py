from collections import Counter
from heapq import heappush, heappop
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        freq_val = [0]*(n+1)
        c = Counter(nums)

        for num, freq in c.items():
            if freq_val[freq] == 0:
                freq_val[freq] = [num]
            else:
                freq_val[freq].append(num)
            
        res = []

        for i in range(n, 0, -1):
            if freq_val[i] != 0:
                res = res + freq_val[i]

            if len(res) == k:
                break
        
        return res