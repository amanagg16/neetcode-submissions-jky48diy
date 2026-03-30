class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF, ROWS, COLS, directions, WATER, TREASURE = (
            2147483647,
            len(grid),
            len(grid[0]),
            [[0, 1], [0, -1], [1, 0], [-1, 0]],
            -1,
            0,
        )

        q = deque()
        # no need to check for visited cells...as the grid values will tell us

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == TREASURE:
                    q.append((i, j))

        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                newr, newc = r + dr, c + dc
                if 0 <= newr < ROWS and 0 <= newc < COLS and grid[newr][newc] == INF:
                    grid[newr][newc] = grid[r][c] + 1
                    q.append((newr, newc))