class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def mergeKLists(lists):
    if len(lists):
        merged = ListNode()
    
    return merged

def mergeTwoLists(list1, list2):
    merged = ListNode(-1, None)
    trav = merged
    
    while list1 and list2:
        if list1.val <= list2.val:
            trav.next = list1
            trav = trav.next
            list1 = list1.next
        else:
            trav.next = list2
            trav = trav.next
            list2 = list2.next
    
    while list1:
        trav.next = list1
        trav = trav.next
        list1 = list1.next
        
    while list2:
        trav.next = list2
        trav = trav.next
        list2 = list2.next
        
    return merged.next
        
def main():    
    list1 = ListNode(1, None)
    list1.next = ListNode(4, None)
    list1.next.next = ListNode(5, None)
    print(list1.val, list1.next.val, list1.next.next.val)
    list2 = ListNode(1, None)
    list2.next = ListNode(3, None)
    list2.next.next = ListNode(4, None)
    print(list2.val, list2.next.val, list2.next.next.val)
    list3 = ListNode(2, ListNode(6, None))
    print(list3.val, list3.next.val)
    
    lists = [list1, list2, list3]
    
    # merged = mergeKLists(lists)
    merged = mergeTwoLists(list1, list2)
    trav = merged
    while(trav != None):
        print(trav.val, end= " ")
        trav = trav.next
    print()
    
main()