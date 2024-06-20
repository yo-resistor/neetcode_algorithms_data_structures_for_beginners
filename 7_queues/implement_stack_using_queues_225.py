import queue

class MyStack:
    def __init__(self):
        self.q = queue.SimpleQueue()
        
    def push(self, x: int) -> None:
        self.q.put(x)
        
    def pop(self) -> int:
        length = self.q.qsize()
        if length == 0:
            return None
        else:
            for i in range(length - 1):
                self.push(self.q.get())
            return self.q.get()
            
    def top(self) -> int:
        length = self.q.qsize()
        if length == 0:
            return None
        else:
            for i in range(length - 1):
                self.push(self.q.get())
            value = self.q.get()
            self.push(value)
            return value
    
    def empty(self) -> bool:
        return self.q.empty()
        
def main():
    stack = MyStack()
    print(stack.empty())
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.pop())
    print(stack.top())
    print(stack.pop())
    

main()