class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # corner case
        if not root:
            return None
        
        result = []
        
        def helper(root: TreeNode) -> None:
            if not root:
                return
            
            helper(root.left)
            result.append(root.val)
            helper(root.right)
            
            return
        
        helper(root)
        
        return result[k - 1]