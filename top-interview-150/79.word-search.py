from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ## next letter in adjenct, then go that path
        ##
        m = len(board)
        n = len(board[0])

        visited = [[False] * n for _ in range(m)]

        def dfs(i: int, j: int, w_idx: int) -> bool:
            if w_idx == len(word):
                return True

            if i < 0 or j < 0 or i >= m or j >= n:
                return False

            if visited[i][j]:
                return False

            if word[w_idx] != board[i][j]:
                return False

            visited[i][j] = True

            up = dfs(i - 1, j, w_idx + 1)
            down = dfs(i + 1, j, w_idx + 1)
            left = dfs(i, j - 1, w_idx + 1)
            right = dfs(i, j + 1, w_idx + 1)

            visited[i][j] = False  # Backtracking: restore state

            return up or down or left or right

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True

        return False
