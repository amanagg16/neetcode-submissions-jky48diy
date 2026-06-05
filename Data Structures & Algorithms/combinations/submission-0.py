class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        output = []

        def dfs(current, i):
            

            if len(current) == k :
                output.append(current.copy())
                return

            
            for j in range(i, n+1):
                current.append(j)
                dfs(current, j+1)
                current.pop()

        dfs([], 1)
        return output