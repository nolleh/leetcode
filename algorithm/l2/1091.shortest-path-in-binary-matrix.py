from queue import Queue


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # constraint: no need to check length of grid
        if grid[0][0] == 1:
            return -1
        q = Queue()
        q.put((0, 0, 1))
        N = len(grid)
        visited = set()
        while q.qsize() > 0:
            x, y, path = q.get()
            if x == N - 1 and y == N - 1:
                if grid[x][y] == 0:
                    return path
                else:
                    return -1
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if x + i < 0 or x + i >= N:
                        continue
                    if y + j < 0 or y + j >= N:
                        continue
                    if (x + i, y + j) in visited:
                        continue
                    elif grid[x + i][y + j] == 0:
                        q.put((x + i, y + j, path + 1))
                    visited.add((x + i, y + j))
        return -1
