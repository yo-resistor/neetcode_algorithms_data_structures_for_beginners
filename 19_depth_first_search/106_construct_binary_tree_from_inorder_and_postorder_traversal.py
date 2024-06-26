class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode:
        # inorder = [9, 3, 15, 20, 7]
        # postorder = [9, 15, 7, 20, 3]

        # base case: if there is nothing in inorder or postorder lists
        if not inorder or not postorder:
            return None

        root = TreeNode(postorder[-1])
        index = inorder.index(root.val)
        
        root.left = self.buildTree(inorder[:index], postorder[:index])
        root.right = self.buildTree(inorder[(index + 1):], postorder[index:-1])
        
        return root