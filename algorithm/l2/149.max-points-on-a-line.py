# HARD
import collections


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # return the maximum number of points that lie on the same straight line
        n = len(points)
        if n == 1:
            return 1

        def calLine(x1, y1, x2, y2):
            if x1 == x2:
                return (1, 0, -x1)
            k = (y1 - y2) / (x1 - x2)
            b = y1 - k * x1
            return (k, -1, b)

        res = 0
        for i in range(n):
            memo = collections.defaultdict(set)
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                line = calLine(x1, y1, x2, y2)
                memo[line].add((x1, y1))
                memo[line].add((x2, y2))
                res = max(res, len(memo[line]))
        return res
