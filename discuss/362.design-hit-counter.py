from collections import deque
class HitCounter:
     
    def __init__(self):
        self.h = deque()
        
    def hit(self, timestamp: int) -> None:
        self.h.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        # [1,2,3]
        while self.h and timestamp - self.h[0] >= 300:
            self.h.popleft()
        return len(self.h)
    
    # TC: O(N) SC: O(N)

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
