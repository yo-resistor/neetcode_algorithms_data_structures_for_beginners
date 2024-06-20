class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        
        while curr:
            trav = curr.next
            curr.next = prev
            prev = curr
            curr = trav
            
        return prev
        
node1 = ListNode(0)
node2 = ListNode(1)
node3 = ListNode(2)
node4 = ListNode(3)

node1.next = node2
node2.next = node3
node3.next = node4

sol = Solution
sol.reverseList(node1)