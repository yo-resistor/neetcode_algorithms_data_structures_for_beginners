class page:
    def __init__(self, url: str):
        self.url = url
        self.prev = None
        self.next = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = page(None)
        self.tail = page(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        
        new = page(homepage)
        new.prev = self.head
        new.next = self.tail
        self.curr = new
        
        self.head.next = new
        self.tail.prev = new

    def visit(self, url: str) -> None:
        new = page(url)
        new.prev = self.curr
        new.next = self.tail
        
        self.curr.next = new
        self.tail.prev = new
        
        self.curr = new
        
    def back(self, steps: int) -> str:
        curr = self.curr
        
        while curr != self.head.next and steps > 0:
            curr = curr.prev
            steps -= 1
            
        self.curr = curr
        
        return self.curr.url
        

    def forward(self, steps: int) -> str:
        curr = self.curr
        while curr != self.tail.prev and steps > 0:
            curr = curr.next
            steps -= 1
            
        self.curr = curr
        
        return self.curr.url
        
    def print(self):
        curr = self.head.next
        
        while curr != self.tail:
            print(curr.url, "->", end=" ")
            curr = curr.next
        print("END")
        
bh = BrowserHistory("leetcode.com")
bh.print()
bh.visit("google.com")
bh.print()
bh.visit("facebook.com")
bh.print()
bh.visit("youtube.com")
bh.print()
print(bh.back(1))
bh.print()
print(bh.back(1))
bh.print()
# bh.visit("linkedin.com")
# bh.print()
print(bh.forward(1))
bh.print()