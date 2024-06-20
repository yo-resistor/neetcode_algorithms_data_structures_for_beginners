class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # base case
        if not head:
            return None
        
        reversed = head
        
        # recursive case
        if head.next:
            reversed = self.reverseList(head.next)
            head.next.next = head
        
        head.next = None
        
        return reversed
        
def main():
    ll = ListNode(1)
    ll.next = ListNode(2)
    ll.next.next = ListNode(3)
    ll.next.next.next = ListNode(4)
    ll.next.next.next.next = ListNode(5)

    print_linked_list(ll)
    
    sol = Solution()
    reversed_ll = sol.reverseList(ll)
    print_linked_list(reversed_ll)
    
def print_linked_list(head: ListNode):
    curr = head
    
    while curr != None:
        print(curr.val, "->", end=" ")
        curr = curr.next
    print(None)
    
if __name__ == "__main__":
    main()