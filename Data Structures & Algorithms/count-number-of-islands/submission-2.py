from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        islands = 0

        q = deque()
        def bfs(r, c):
            q.append((r, c))

            while q:
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                r, c = q.popleft()        
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if nr in range(rows) and nc in range(cols) and grid[nr][nc] == "1":
                        q.append((nr, nc))
                        grid[nr][nc] = "0"

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1
        return islands