class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def main():
    list1 = ListNode(1)
    list1.next = ListNode(2)
    list1.next.next = ListNode(4)
    
    list2 = ListNode(1)
    list2.next = ListNode(3)
    list2.next.next = ListNode(5)
    
    print(getValues(list1), getValues(list2))
    print(getValues(mergeTwoLists(list1, list2)))
    
def mergeTwoLists(list1: ListNode, list2: ListNode):
    sorted = ListNode()
    curr = sorted
    
    while list1 and list2:
        if list1.val < list2.val:
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2
            list2 = list2.next
        curr = curr.next
            
    curr.next = list1 or list2
            
    return sorted.next
    
def getValues(head: ListNode) -> list[int]:
    values = []
    curr = head
    while curr:
        values.append(curr.val)
        curr = curr.next
        
    return values

main()