from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        q = deque()
        num_fresh = 0
        FRESH, ROTTEN = 1, 2

        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == FRESH:
                    num_fresh += 1
                elif grid[i][j] == ROTTEN:
                    q.append((i,j))
        
        if num_fresh == 0:
            return 0
        if num_fresh > 0 and len(q) == 0:
            return -1
        minutes = 0
        directions = [[1,0],[-1,0],[0, 1],[0, -1]]
        while q and num_fresh:

            for i in range(len(q)):
                r,c = q.popleft()
                for dr, dc in directions:
                    newR, newC = r + dr, c + dc
                    if 0<=newR<ROW and 0<=newC<COL and grid[newR][newC] == FRESH:
                        grid[newR][newC] = ROTTEN
                        q.append((newR, newC))
                        num_fresh -= 1

            minutes += 1

        return minutes if num_fresh == 0 else -1
