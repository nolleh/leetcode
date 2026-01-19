from typing import List
from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)

        visited = [0] * numCourses

        def hasCycle(i: int) -> bool:
            if visited[i] == 1:
                return True
            if visited[i] == 2:
                return False

            visited[i] = 1
            for j in graph[i]:
                if hasCycle(j):
                    return True
            visited[i] = 2

            return False

        for i in range(numCourses):
            if hasCycle(i):
                return False
        return True
