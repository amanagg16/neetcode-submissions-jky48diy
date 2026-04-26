from collections import deque
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        q = deque()
        indegree = [0]*numCourses
        adj_list = [[] for _ in range(numCourses)]

        for v, u in prerequisites: # notice the reverse of edges as edges mentioned in question are in reverse order
            indegree[v] += 1
            adj_list[u].append(v)
        
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
            
        topo_count = 0
        topo = []
        while q:
            node = q.popleft()
            topo_count+=1
            topo.append(node)
            for nei in adj_list[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
                
            
        return topo if topo_count == numCourses else []