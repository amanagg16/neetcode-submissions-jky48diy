from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        class DSU:
            def __init__(self, n):
                self.par = [i for i in range(n)]
                self.rank = [0]*n
                self.components = n


            def find(self, x):
                if self.par[x] == x:
                    return x

                self.par[x] = self.find(self.par[x])
                return self.par[x]
            
            def union(self, x, y):
                rx, ry = self.find(x), self.find(y)
                if rx == ry:
                    return False

                self.components -= 1
                if self.rank[rx] < self.rank[ry]:
                    self.par[rx] = ry
                elif self.rank[rx] > self.rank[ry]:
                    self.par[ry] = rx
                else:
                    self.par[rx] = ry
                    self.rank[ry] += 1
                
                return True
            
            def get_component(self):
                return self.components 
            
        dsu = DSU(n)

        for u, v in edges:
            if not dsu.union(u, v):
                return False
        
        return True if dsu.get_component() == 1 else False