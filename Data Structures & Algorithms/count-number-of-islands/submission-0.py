class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        num_islands = 0
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        
        def bfs(x,y):
            grid[x][y] = "0"
            q = deque()
            q.append((x,y))
            

            while q:
                r,c = q.popleft()

                for dr,dc in directions:
                    newR, newC = r+dr, c+dc
                    if 0<=newR<ROW and 0<=newC<COL and grid[newR][newC] == "1":
                        q.append((newR, newC))
                        grid[newR][newC] = "0"


        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == "1":
                    num_islands+=1
                    bfs(i,j)

        return num_islands