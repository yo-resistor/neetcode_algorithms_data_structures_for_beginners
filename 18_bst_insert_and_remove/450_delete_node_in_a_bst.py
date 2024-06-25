class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        # corner case
        if not root:
            return root
        
        # find the target node
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        # at the target node
        else:
            # case 1: 0 or 1 child
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            # case 2: 2 children
            else:
                minNode = self.minValueNode(root.right)
                root.val = minNode.val
                root.right = self.deleteNode(root.right, minNode.val)
        
        return root
        
    def minValueNode(self, root: TreeNode) -> TreeNode:
        curr = root
        
        while curr and curr.left:
            curr = curr.left
        
        return curr