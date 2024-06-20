class ListNode:
    def __init__(self, val = -1, next = None):
        self.val = val
        self.next = next

class Deque:
    def __init__(self):
        self.head = self.tail = None

    def isEmpty(self) -> bool:
        return self.head == None

    def append(self, value: int) -> None:
        new = ListNode(value)

        # when queue is empty
        if not self.head:
            self.head = self.tail = new
        # when queue is not empty
        else:
            self.tail.next = new
            self.tail = new
        
    def appendleft(self, value: int) -> None:
        new = ListNode(value)

        # when queue is empty
        if not self.head:
            self.head = self.tail = new
        # when queue is not empty
        else:
            new.next = self.head
            self.head = new

    def pop(self) -> int:
        # when queue is empty
        if self.head == None:
            return -1
        # when queue has one element
        elif self.head == self.tail:
            value = self.tail.val
            self.head = self.tail = None
            return value
        # when queue has more than one element
        else:
            curr = self.head
            while curr.next.next:
                curr = curr.next
                
            value = curr.next.val
            self.tail = curr
            self.tail.next = None
            
            return value

    def popleft(self) -> int:
        # when queue is empty
        if not self.head:
            return -1
        # when queue has one element
        elif self.head == self.tail:
            value = self.head.val
            self.head = self.tail = None
            return value
        # when queue has more than one element
        else:
            value = self.head.val
            self.head = self.head.next
            return value
    
    def getvalues(self) -> list[int]:
        values = []
        curr = self.head
        while curr:
            values.append(curr.val)
            curr = curr.next
        
        return values

def main():
    queue = Deque()
    queue.appendleft(1)
    print(queue.getvalues())
    queue.appendleft(2)
    print(queue.getvalues())
    print(queue.pop())
    print(queue.getvalues())
    
main()
