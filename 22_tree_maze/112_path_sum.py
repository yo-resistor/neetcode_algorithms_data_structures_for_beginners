class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        pathValues = []
        return self.hasPathSumHelper(root, targetSum, pathValues)
        
    def hasPathSumHelper(self, root: TreeNode, targetSum: int, pathValues: list[int]) -> bool:
    # concept: record values of path down to leaf node
        # corner case: if there is no tree
        if root is None:
            return False
        
        # push root value to path
        pathValues.append(root.val)
        
        # base case: the node is leaf node
        if root.left is None and root.right is None:
            return True
        
        # recursive case on the left sub-tree
        if self.hasPathSumHelper(root.left, targetSum, pathValues):
            # compare sum of values in the path and targetSum
            if sum(pathValues) == targetSum:
                return True
            # pop the value from the path when backtracking
            else:
                pathValues.pop()
            
        # recursive case on the right sub-tree
        if self.hasPathSumHelper(root.right, targetSum, pathValues):
            # compare sum of values in the path and targetSum
            if sum(pathValues) == targetSum:
                return True
            # pop the value from the path when backtracking
            else:
                pathValues.pop()
            
        # if there is not valid path
        return False