class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
def main():
    list1 = ListNode(1, None)
    list1.next = ListNode(2, None)
    list1.next.next = ListNode(4, None)   
    list2 = ListNode(1, None)
    list2.next = ListNode(3, None)
    list2.next.next = ListNode(4, None)  
    
    # list1 = None
    # list2 = None
    
    print(getValues(list1), getValues(list2))
    print(getValues(mergeLists_iterative(list1, list2)))

def mergeLists_iterative(list1: ListNode, list2: ListNode) -> ListNode:
    merged = ListNode()
    curr = merged
    
    while list1 and list2:
        if list1.val < list2.val:
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2
            list2 = list2.next
        curr = curr.next
        
    curr.next = list1 or list2
            
    return merged.next


def getValues(head: ListNode) -> list[int]:
    values = []
    curr = head
    while curr:
        values.append(curr.val)
        curr = curr.next
    return values


main()