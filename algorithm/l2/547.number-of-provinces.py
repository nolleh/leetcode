class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(i: int, visited):
            for j in range(len(isConnected[i])):
                if j not in visited and i != j and isConnected[i][j] == 1:
                    visited.add(j)
                    dfs(j, visited)

        visited = set()
        count = 0
        for i in range(len(isConnected)):
            if i not in visited:
                count = count + 1
            dfs(i, visited)
        return count
