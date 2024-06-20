class MinStack:
    def __init__(self):
        self.stack = []
        self.min = []
    
    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.min.append(val)
        else:
            if self.min[-1] < val:
                self.min.append(self.min[-1])
            else:
                self.min.append(val)
                
        self.stack.append(val)
    
    def pop(self) -> None:
        if len(self.stack) > 0:
            self.stack.pop()
            self.min.pop()
    
    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1]    
        else:
            return None
    
    def getMin(self) -> int:
        return self.min[-1]


stack = MinStack()
print(stack.stack)
print(stack.push(-2))
print(stack.push(0))
print(stack.push(-3))
print(stack.getMin())
print(stack.pop())
print(stack.top())
print(stack.getMin())
