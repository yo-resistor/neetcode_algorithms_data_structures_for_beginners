from collections import deque

class Graph:
    def __init__(self):
        self.adjList = dict()
        
    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.adjList:
            self.adjList[src] = []
        if dst not in self.adjList:
            self.adjList[dst] = []
        self.adjList[src].append(dst)
        return
    
    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.adjList or dst not in self.adjList[src]:
            return False
        self.adjList[src].remove(dst)
        return True
    
    def hasPath(self, src: int, dst: int) -> bool:
        def bfs(start, end, adjList) -> bool:
            length = 0
            visit = set()
            visit.add(start)
            queue = deque()
            queue.append(start)
            
            while queue:
                for _ in range(len(queue)):
                    curr = queue.popleft()
                    if curr == end and length > 0:
                        return True
                    
                    for neighbor in adjList[curr]:
                        if neighbor not in visit:
                            visit.add(neighbor)
                            queue.append(neighbor)
                length += 1
            return False
                
        return bfs(src, dst, self.adjList)
        
def main():
    print("Graph 1:")
    graph1 = Graph()
    graph1.addEdge(1, 2)
    print(graph1.adjList)
    graph1.addEdge(2, 3)
    print(graph1.adjList)
    print(graph1.adjList, graph1.hasPath(1, 3))
    print(graph1.adjList, graph1.hasPath(3, 1))
    print(graph1.adjList, graph1.removeEdge(1, 2))
    print(graph1.adjList, graph1.hasPath(1, 3))
    
    print("Graph 2")
    graph2 = Graph()
    graph2.addEdge(1, 2)
    print(graph2.adjList)
    graph2.addEdge(2, 3)
    print(graph2.adjList)
    graph2.addEdge(3, 1)
    print(graph2.adjList)
    print(graph2.adjList, graph2.hasPath(1, 3))
    print(graph2.adjList, graph2.hasPath(3, 1))
    
if __name__ == "__main__":
    main()