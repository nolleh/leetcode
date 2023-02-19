from queue import Queue
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return -1

        q = Queue()
        q.put('0000')
        step = 0
        visit = set()
        while not q.empty():
            s = q.qsize()
            
            for _ in range(s):
                c = q.get()
                if c == target:
                    return step
                for j in range(4):
                    left = c[:j]
                    right = c[j+1:]

                    def put(nxt): 
                        ncode = left + str(nxt) + right
                        if ncode not in deadends and ncode not in visit:
                            visit.add(ncode)
                            q.put(ncode)

                    put((int(c[j]) - 1) % 10)
                    put((int(c[j]) + 1) % 10)
            step+=1
        return -1
