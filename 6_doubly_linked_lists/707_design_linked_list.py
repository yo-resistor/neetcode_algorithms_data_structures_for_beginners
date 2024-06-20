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
        
    def get(self, index: int) -> int:
        curr = self.head.next
        
        while curr and index > 0:
            curr = curr.next
            index -= 1
            
        if curr and curr != self.tail and index == 0:
            return curr.val
        
        return -1
            
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
        
    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.head.next
        
        while curr and index > 0:
            curr = curr.next
            index -= 1
        
        if curr and index == 0:    
            new = ListNode(val)
            new.prev = curr.prev
            new.next = curr
            
            curr.prev.next = new
            curr.prev = new
        
    def deleteAtIndex(self, index: int) -> None:
        curr = self.head.next
        
        while curr and index > 0:
            curr = curr.next
            index -= 1
            
        if curr and curr != self.tail and index == 0:
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
        
    def print(self):
        curr = self.head.next
        
        while curr != self.tail:
            print(curr.val, "->", end=" ")
            curr = curr.next
        print(None)

linked_list = MyLinkedList()
linked_list.addAtHead(1)
linked_list.addAtTail(3)
linked_list.print()
linked_list.addAtIndex(1, 2)
linked_list.print()
print(linked_list.get(1))
linked_list.deleteAtIndex(1)
linked_list.print()
print(linked_list.get(1))