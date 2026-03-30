"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited_to_cloned = {}

        def dfs(node):
            if not node:
                return None
            
            if node in visited_to_cloned:
                return visited_to_cloned[node]
            
            cloned = Node(node.val)
            visited_to_cloned[node] = cloned

            for nei in node.neighbors:
                cloned.neighbors.append(dfs(nei))

            return cloned

        return dfs(node)