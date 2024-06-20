from queue import Queue

class MyStack:
    def __init__(self):
        self.q = Queue()
        
    def push(self, x: int) -> None:
        self.q.put(x)
        
    def pop(self) -> int:
        for _ in range(self.q.qsize() - 1):
            self.q.put(self.q.get())
        return self.q.get()
        
    def top(self) -> int:
        for _ in range(self.q.qsize() - 1):
            self.q.put(self.q.get())
        value = self.q.get()
        self.q.put(value)
        return value
        
    def empty(self) -> None:
        return Queue.empty(self.q)
        

obj = MyStack()
obj.push(1)
obj.push(2)
print(obj.top())
print(obj.pop())
print(obj.empty())
print(obj.pop())
print(obj.empty())
