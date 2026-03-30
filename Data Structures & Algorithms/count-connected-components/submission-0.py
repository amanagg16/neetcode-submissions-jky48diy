class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = 0
        visited = set()
        adj_list = [[] for _ in range(n)]

        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        def bfs(i):
            q = deque()
            q.append(i)
        
            while q:
                u = q.popleft()
                visited.add(u)
                for nei in adj_list[u]:
                    if nei not in visited:
                        q.append(nei)
                
        for i in range(n):
            if i not in visited:
                bfs(i)
                res += 1
        
        return res