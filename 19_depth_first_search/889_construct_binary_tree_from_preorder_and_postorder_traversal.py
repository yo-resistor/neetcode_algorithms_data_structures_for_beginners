class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructFromPrePost(self, preorder: list[int], postorder: list[int]) -> TreeNode:
        # preorder = [1,2,4,5,3,6,7]
        # postorder = [4,5,2,6,7,3,1]
        
        # corner case: if there is nothing in preorder or postorder lists
        if not preorder or not postorder:
            return None
        
        root = TreeNode(postorder.pop())
        if len(preorder > 1):
            # there are more than one element in the tree
            index = preorder.index(postorder[-1])
            root.right = self.constructFromPrePost(preorder[index:], postorder)
            root.left = self.constructFromPrePost(preorder[1:index], postorder)
        
        return root