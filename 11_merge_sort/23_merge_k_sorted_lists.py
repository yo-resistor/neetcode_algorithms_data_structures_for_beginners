class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None
        
class Solution:
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        # corner case
        if not lists or len(lists) == 0:
            return None
        
        # run merge algorithm while there's only one list remaining in the array
        while len(lists) > 1:
            lists_merged = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i + 1] if i + 1 < len(lists) else None
                lists_merged.append(self.merge(list1, list2))
            lists = lists_merged
            
        return lists[0]
        
    def merge(self, list1: ListNode, list2: ListNode) -> ListNode:
        # set a dummy header in merged linked list
        merged = ListNode(-1)
        # list1 and list2 are already sorted
        
        # set three pointers: i in list1, j in list2, k in merged
        i, j, k = list1, list2, merged
        
        # i pointer is in list1 and j pointer is in list2
        while i and j:
            if i.val <= j.val:
                k.next = ListNode(i.val, None)
                k = k.next
                i = i.next
            else:
                k.next = ListNode(j.val, None)
                k = k.next
                j = j.next
        
        # i pointer is in list1 and j pointer is out of list2
        while i:
            k.next = ListNode(i.val, None)
            k = k.next
            i = i.next
        
        # i pointer is out of list1 and j pointer is in list2
        while j:
            k.next = ListNode(j.val, None)
            k = k.next
            j = j.next
        
        # return merged linked list excluding dummy header
        return merged.next
    
    def print(self, list: ListNode) -> None:
        curr = list
        
        while curr:
            print(curr.val, "->", end=" ")
            curr = curr.next
        print(None)
        
def main():
    list1 = ListNode(1)
    list1.next = ListNode(2)
    list1.next.next = ListNode(4)
    
    list2 = ListNode(1)
    list2.next = ListNode(3)
    list2.next.next = ListNode(5)
    
    list3 = ListNode(3)
    list3.next = ListNode(6)
    
    sol = Solution()
    sol.print(list1)
    sol.print(list2)
    sol.print(list3)
    
    sol.print(sol.merge(list1, list2))
    sol.print(sol.mergeKLists([list1, list2, list3]))
    
if __name__ == "__main__":
    main()