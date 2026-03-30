class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        max_area = 0
        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        def get_graph_area(x, y):
            q = deque()
            q.append((x,y))
            grid[x][y] = 0
            area = 0

            while q:
                r, c = q.popleft()
                area += 1
                for dr,dc in directions:
                    newR, newC = r + dr, c + dc
                    if 0<=newR<ROW and 0<=newC<COL and grid[newR][newC] == 1:
                        grid[newR][newC] = 0
                        q.append((newR, newC))
            return area


        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 1:
                    max_area = max(max_area, get_graph_area(i,j))

        return max_area