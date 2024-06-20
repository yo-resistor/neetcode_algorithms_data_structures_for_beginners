class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
    
def main():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    print(getValues(head))
    reverse = reverseList_iterative(head)
    print(getValues(reverse))
    
def reverseList_iterative(head: ListNode) -> ListNode:
    prev = None
    next = head
    
    while next:
        trav = next.next
        next.next = prev
        prev = next
        next = trav
    
    return prev

# def reverseList_recursive(head: ListNode) -> ListNode:
    

def getValues(head: ListNode) -> list[int]:
    values = []
    curr = head
    while curr:
        values.append(curr.val)
        curr = curr.next
    return values

main()