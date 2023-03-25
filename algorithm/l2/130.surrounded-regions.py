class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        # for first and last rows
        for i in [0, len(board) - 1]:
            for j in range(len(board[0])):
                self.dfs(board, i, j)
        # for first and last cols
        for i in range(len(board)):
            for j in [0, len(board[0]) - 1]:
                self.dfs(board, i, j)
        # now, we changed all 'O' to '.' which connected to edge 'O'
        # until now remaining 'O' need to be filped to 'X'
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == ".":
                    board[i][j] = "O"

    def dfs(self, board, i, j):
        ## not edged 'O' fliped to .
        if 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == "O":
            board[i][j] = "."
            self.dfs(board, i + 1, j)
            self.dfs(board, i - 1, j)
            self.dfs(board, i, j + 1)
            self.dfs(board, i, j - 1)
