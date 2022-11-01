from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q = deque()
        DEFAULT = 0
        output = [[DEFAULT for j in range(len(mat[i]))] for i in range(len(mat))]
        
        for r in range(len(mat)):
            for c in range(len(mat[r])):
                if mat[r][c] == 0:
                    q.append((r, c, 0))
                    output[r][c] = 0
        visited = set()
        while q:
            row, col, depth = q.popleft()
            if (row, col) in visited:
                continue
            
            visited.add((row, col))
            if output[row][col] == DEFAULT:
                output[row][col] = depth

            if row > 0 and (row - 1, col) not in visited and output[row - 1][col] == DEFAULT:
                q.append((row - 1, col, depth + 1))
            if row < len(mat) -1 and (row + 1, col) not in visited and output[row +1][col] == DEFAULT:
                q.append((row + 1, col, depth + 1))
            if col > 0 and (row, col -1) not in visited and output[row][col - 1] == DEFAULT:
                q.append((row, col -1, depth +1))
            if col < len(mat[row]) -1 and (row, col + 1) not in visited and output[row][col + 1] == DEFAULT:
                q.append((row, col + 1, depth +1))
        return output
