class Stack:
    def __init__(self):
        self.stack = []
    def push(self, x: int) -> None:
        self.stack += [x]
    def pop(self) -> int:
        return self.stack.pop()
    def top(self) -> int:
        return self.stack[-1]
    def size(self) -> int:
        return len(self.stack)
    def empty(self) -> bool:
        return len(self.stack) == 0

class MyQueue:

    def __init__(self):
        self.stack = Stack()

    def push(self, x: int) -> None:
        self.stack.push(x) 

    def pop(self) -> int:
        if self.stack.empty():
            return -1
        self.stack2 = Stack()
        while not self.stack.empty():
            self.stack2.push(self.stack.pop()) 
        first = self.stack2.pop()
        while not self.stack2.empty():
            self.stack.push(self.stack2.pop())
        return first

    def peek(self) -> int:
        if self.stack.empty():
            return -1
        self.stack2 = Stack() 
        while not self.stack.empty():
            self.stack2.push(self.stack.pop())
        first = self.stack2.top()
        while not self.stack2.empty():
            self.stack.push(self.stack2.pop())
        return first 

    def empty(self) -> bool:
        return self.stack.empty() 


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
