class BrowserNode:
    def __init__(self, url = None):
        self.url = url
        self.prev = None
        self.next = None
    
class BrowserHistory:
    def __init__(self, homepage: str):
        self.start = BrowserNode()
        self.end = BrowserNode()
        self.curr = BrowserNode(homepage)
        
        self.start.next = self.curr
        self.end.prev = self.curr
        
        self.curr.prev = self.start
        self.curr.next = self.end
    
    def visit(self, url: str) -> None:
        new = BrowserNode(url)
        new.prev = self.curr
        new.next = self.end
        
        self.curr.next = new
        self.end.prev = new
        
        self.curr = new
        
    def back(self, steps: int) -> str:
        while self.curr and steps > 0:
            self.curr = self.curr.prev
            steps -= 1
        
        if self.curr and self.curr != self.start and steps == 0:
            return self.curr.url
        else:
            self.curr = self.start.next
            return self.curr.url
        
    def forward(self, steps: int) -> str:
        while self.curr and steps > 0:
            self.curr = self.curr.next
            steps -= 1
            
        if self.curr and self.curr != self.end and steps == 0:
            return self.curr.url
        else:
            self.curr = self.end.prev
            return self.curr.url
        
    def geturl(self) -> list[str]:
        urls = []
        trav = self.start.next
        while trav and trav != self.end:
            urls.append(trav.url)
            trav = trav.next
        
        return urls
        
def main():
    history = BrowserHistory("leetcode.com")
    print(history.geturl())
    history.visit("google.com")
    print(history.geturl())
    history.visit("facebook.com")
    print(history.geturl())
    history.visit("youtube.com")
    print(history.geturl())
    print(history.back(1))
    print(history.geturl())
    history.visit("linkedin.com")
    print(history.geturl())
    print(history.back(7))
    print(history.geturl())
    print(history.forward(1))
    print(history.geturl())
    history.visit("yunsikohm.com")
    print(history.geturl())
    

main()