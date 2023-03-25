from queue import Queue


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        if n <= 1:
            return []
        q = Queue()
        q.put((0, [0]))
        output = []
        while q.qsize() > 0:
            x, p = q.get()
            if x == n - 1:
                output.append(p)
                continue
            for d in graph[x]:
                # print(d, p + [d])
                q.put((d, p + [d]))
        return output
