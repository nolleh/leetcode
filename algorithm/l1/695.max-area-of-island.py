class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(i: int, j: int, visit: dict) -> int:
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]):
                return 0
            if grid[i][j] == 0:
                return 0
            if (i, j) in visit:
                return 0

            visit[(i, j)] = True

            f1 = dfs(i - 1, j, visit)
            f2 = dfs(i + 1, j, visit)
            f3 = dfs(i, j - 1, visit)
            f4 = dfs(i, j + 1, visit)
            return 1 + f1 + f2 + f3 + f4

        max_area = 0
        visit = {}
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (i, j) not in visit:
                    max_area = max(max_area, dfs(i, j, visit))
        return max_area
