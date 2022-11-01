from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        output = [[sys.maxsize for _ in range(len(grid[i]))] for i in range(len(grid))]
        q = deque()
        visited = set()
        max_dist = 0 
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 2:
                    q.append((r, c, 0))
        
        while q:
            r, c, dist = q.popleft()
            output[r][c] = min(output[r][c], dist)
            max_dist = max(max_dist, output[r][c])
            visited.add((r,c)) 
            if r > 0 and (r - 1, c) not in visited and grid[r-1][c] == 1:
                # if next is rooten, initialize dist as 0
                n_dist = dist + 1 if grid[r -1][c] == 1 else 0
                q.append((r -1, c, n_dist))
            if r < len(grid) -1 and (r + 1, c) not in visited and grid[r+1][c] == 1:
                n_dist = dist + 1 if grid[r+1][c] == 1 else 0
                q.append((r+1, c, n_dist))
            if c > 0 and (r, c -1) not in visited and grid[r][c -1] == 1:
                n_dist = dist + 1 if grid[r][c-1] == 1 else 0
                q.append((r, c -1, n_dist))
            if c < len(grid[r]) -1 and (r, c + 1) not in visited and grid[r][c + 1] == 1:
                n_dist = dist + 1 if grid[r][c +1] == 1 else 0
                q.append((r, c + 1, n_dist))
        
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if (r,c) not in visited and grid[r][c] == 1:
                    return -1
        return max_dist
