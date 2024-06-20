class MinStack:
    def __init__(self):
        self.stack = []
        self.min = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min) == 0:
            self.min.append(val)
        else:
            if self.min[-1] > val:
                self.min.append(val)
            else:
                self.min.append(self.min[-1])
    
    def pop(self) -> None:
        if len(self.stack) > 0:
            self.stack.pop()
            self.min.pop()
        
    def top(self) -> int:
        return self.stack[-1]
    
    def getMin(self) -> int:
        return self.min[-1]
    
minstack = MinStack()
minstack.push(-2)
minstack.push(0)
minstack.push(-3)
print(minstack.getMin())
minstack.pop()
print(minstack.top())
print(minstack.getMin())
