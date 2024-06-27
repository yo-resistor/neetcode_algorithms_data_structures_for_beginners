from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        queue = deque()
        results = []
        
        if root:
            queue.append(root)
        
        # level = 0
        while len(queue) > 0:
            result = []
            for _ in range(len(queue)):
                curr = queue.popleft()
                result.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            # level += 1
            results.append(result)
                
        return results
    