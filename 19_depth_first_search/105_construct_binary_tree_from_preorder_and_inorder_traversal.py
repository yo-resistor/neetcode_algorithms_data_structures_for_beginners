class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        # preorder = [3, 9, 20, 15, 7]
        # inorder = [9, 3, 15, 20, 7]
        
        # base: if there is nothing in preorder or inorder lists
        if not preorder or not inorder:
            return None
        
        root = TreeNode(val = preorder[0])
        index = inorder.index(root.val)
        
        inorder_left = inorder[:index]
        preorder_left = preorder[1:(index + 1)]
        inorder_right = inorder[(index + 1):]
        preorder_right = preorder[(index + 1):]
        
        root.left = self.buildTree(preorder_left, inorder_left)
        root.right = self.buildTree(preorder_right, inorder_right)
        
        return root