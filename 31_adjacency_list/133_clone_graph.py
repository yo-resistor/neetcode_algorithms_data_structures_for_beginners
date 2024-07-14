class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
class Solution:
    def cloneGraph(self, node: Node) -> Node:
        oldToNew = dict()
        
        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            
            new = Node(node.val)
            oldToNew[node] = new
            for neighbor in node.neighbors:
                new.neighbors.append(dfs(neighbor))
                
            return new
        return dfs(node) if node else None