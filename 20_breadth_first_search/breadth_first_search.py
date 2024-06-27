from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def bfs(root: TreeNode):
        queue = deque()
        
        if root:
            queue.append(root)
            
        level = 0
        while len(queue) > 0:
            print("level:", level)
            curr = queue.popleft()
            print(curr.val)
            if curr.left:
                queue.apeend(curr.left)
            if curr.right:
                queue.append(curr.right)