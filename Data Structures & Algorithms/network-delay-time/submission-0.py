from collections import defaultdict
from heapq import heappop, heappush
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        min_times = {}  # we don't initialize with k as then we wont be able to add its neighbors in the heap
        max_time = -1
        min_heap = [(0, k)]
        while min_heap:
            min_time, node = heappop(min_heap)
            if node in min_times:
                continue

            min_times[node] = min_time
            max_time = max(max_time, min_time)

            for nei, time in graph[node]:
                if nei not in min_times:
                    heappush(min_heap, (min_time + time, nei))

        return max_time if len(min_times) == n else -1