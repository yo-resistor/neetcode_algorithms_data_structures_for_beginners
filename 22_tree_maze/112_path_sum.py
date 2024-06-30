class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        # corner case: if root node is empty
        if root is None:
            return False
        
        targetSum -= root.val
        
        # check whether remaining targetSum is zero at leaf node
        if root.left is None and root.right is None:
            if targetSum == 0:
                return True
            else:
                targetSum += root.val
                return False
        
        # recursive case in sub-trees
        return (self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum))