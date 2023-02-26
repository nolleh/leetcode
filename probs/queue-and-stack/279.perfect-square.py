from queue import Queue
import math


class Solution:
    def numSquares(self, n: int) -> int:
        # return the least number of perfect square nmbers that sum to 'n'
        # perfect sqaure is is the square of an integer; n^2 (i.e, 1,4,9,16...)

        # ex. 12 -> 3 (4 + 4 + 4)
        # ex. 13 -> 2 (4 + 9)

        # insight: shortest # of sum.

        if n == 1:
            return 1
        q = Queue()
        q.put(n)
        step = 0

        while not q.empty():
            s = q.qsize()
            for _ in range(s):
                t = q.get()
                if t == 0:
                    return step
                mx = int(math.sqrt(n))
                for i in range(mx, 0, -1):
                    nt = t - i * i
                    if nt == 0:
                        return step + 1
                    elif nt > 0:
                        q.put((nt))
            step += 1
        return -1
