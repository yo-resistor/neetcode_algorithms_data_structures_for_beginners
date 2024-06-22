class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        # If there is no root node
        if not root:
            return None
        
        # If there is root node, compare the values
        if root.val > val:
            return self.searchBST(root.right, val)
        elif root.val < val:
            return self.searchBST(root.left, val)
        else:
            return root