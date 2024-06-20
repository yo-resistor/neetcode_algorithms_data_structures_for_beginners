class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None
        

class MyLinkedList:
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def addAtHead(self, val: int) -> None:
        new = ListNode(val)
        new.prev = self.head
        new.next = self.head.next
        
        self.head.next.prev = new
        self.head.next = new
        
    def addAtTail(self, val: int) -> None:
        new = ListNode(val)
        new.prev = self.tail.prev
        new.next = self.tail
        
        self.tail.prev.next = new
        self.tail.prev = new
        
    def get(self, index: int) -> int:
        curr = self.head.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        
        if curr and curr != self.tail and index == 0:
            return curr.val
        else:
            return -1
        
    def addAtIndex(self, index: int, val: int) -> None:
        new = ListNode(val)
        curr = self.head
        for i in range(index + 1):
            curr = curr.next
            if curr == self.tail:
                return
        else:
            new.prev = curr.prev
            new.next = curr
            
            curr.prev.next = new
            curr.prev = new
            
    def deleteAtIndex(self, index: int) -> None:
        curr = self.head
        for i in range(index + 1):
            curr = curr.next
            if curr == self.tail:
                return
        else:
            curr.next.prev = curr.prev
            curr.prev.next = curr.next
        
        
        
    def getValues(self) -> list[int]:
        values = []
        curr = self.head.next
        while curr.next:
            values.append(curr.val)
            curr = curr.next
        
        return values
        
        
def main():
    list1 = MyLinkedList()
    list1.addAtHead(7)
    print(list1.getValues())
    list1.addAtHead(2)
    print(list1.getValues())
    list1.addAtHead(1)
    print(list1.getValues())
    list1.addAtIndex(3, 0)
    print(list1.getValues())
    list1.addAtHead(2)
    print(list1.getValues())
    list1.addAtTail(6)
    print(list1.getValues())
    print(list1.get(4))
    list1.addAtHead(4)
    print(list1.getValues())
    list1.addAtIndex(5, 0)
    print(list1.getValues())
    list1.addAtHead(6)
    print(list1.getValues())
    list1.deleteAtIndex(2)
    print(list1.getValues())
    

main()