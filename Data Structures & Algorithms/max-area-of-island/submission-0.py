from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        visited = set()

        max_area = 0
        c_area = 0
        def bfs(r, c):
            visited.add((r, c))
            q = deque()
            q.append((r, c))

            area = 1
            while q:
                r, c = q.popleft()
                directions = [[1,0], [-1,0], [0,1], [0,-1]]

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr in range(rows) and nc in range(cols) and grid[nr][nc] == 1 and (nr, nc) not in visited:
                        q.append((nr, nc))
                        visited.add((nr, nc))
                        area += 1
            return area


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    c_area = bfs(r, c)
                    max_area = max(c_area, max_area)
        return max_area


