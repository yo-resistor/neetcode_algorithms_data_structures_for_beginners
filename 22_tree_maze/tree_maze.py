class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def canReachLeaf(root):
    # base case if root doesn't exist or root value is 0
    if not root or root.val == 0:
        return False
    
    # check whether the node is leaf node or not
    if root.left is None and root.right is None:
        return True
    
    # recursive case on left sub-tree
    if canReachLeaf(root.left):
        return True
    
    # recursive case on right sub-tree
    if canReachLeaf(root.right):
        return True
    
    # if there is not valid path (all paths are blocked)
    return False

def findPath(root, path):
    # base case if root doesn't exist or root value is 0
    if not root or root.val == 0:
        return False
    
    # push the value to the path
    path.append(root.val)
    
    # check whether the node is leaf node or not
    if root.left is None and root.right is None:
        return True
    
    # recursive case on left sub-tree
    if findPath(root.left):
        return True
    
    # recursive case on right sub-tree
    if findPath(root.right):
        return True
    
    # pop the value from the path when backtracking
    path.pop()
    
    # if there is not valid path (all paths are blocked)
    return False