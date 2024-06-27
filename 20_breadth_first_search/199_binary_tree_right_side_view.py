from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def rightSideView(self, root: TreeNode) -> list[int]:
        queue = deque()
        result = []
        
        if root:
            queue.append(root)
        
        level = 0
        while queue:
            values = []
            for _ in range(len(queue)):
                curr = queue.popleft()
                values.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            level += 1
            result.append(values[-1])
        
        return result