from heapq import heappush, heappop
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])

        min_heap = [(0, 0, 0)]  # difference of node from 0,0
        visited = set()
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        while min_heap:
            diff, r, c = heappop(min_heap)
            if (r, c) in visited:
                continue
            if r == ROWS - 1 and c == COLS - 1:
                return diff
            visited.add((r, c))

            for dr, dc in directions:
                newR, newC = r + dr, c + dc
                if (
                    0 <= newR < ROWS
                    and 0 <= newC < COLS
                    and (newR, newC) not in visited
                ):
                    new_diff = max(diff, abs(heights[r][c] - heights[newR][newC]))
                    heappush(min_heap, (new_diff, newR, newC))