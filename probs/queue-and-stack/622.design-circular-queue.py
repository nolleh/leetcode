class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [0] * k
        self.head = 0
        self.tail = 0
        self.len = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.q[self.tail] = value
        self.tail = (self.tail + 1) % len(self.q)
        self.len+=1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False 
        self.head = (self.head + 1) % len(self.q) 
        self.len-=1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.tail -1] 

    def isEmpty(self) -> bool:
        return self.len == 0
    
    def isFull(self) -> bool:
        return self.len == len(self.q)
