class TreeNode:
    def __init__(self, key: int, val: int, left=None, right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right

class TreeMap:
    def __init__(self):
        self.root = None
        
    def insert(self, key: int, val: int) -> None:
        # if there is nothing in root node, insert at root
        if not self.root:
            self.root = TreeNode(key=key, val=val)
            return
        
        # if there are nodes in the tree aleady, find the correct spot
        curr = self.root
        while True:
            # new key is larger -> right sub tree
            if key > curr.key:
                if curr.right is None:
                    curr.right = TreeNode(key=key, val=val)
                    return
                curr = curr.right
            # new key is smaller -> left sub tree
            elif key < curr.key:
                if curr.left is None:
                    curr.left = TreeNode(key=key, val=val)
                    return
                curr = curr.left
            # new key is already present, override the original with the new
            else:
                curr.val = val
                return
    
    def get(self, key: int) -> int:
        # if there is nothing in root node, return -1
        if not self.root:
            return -1
        
        # if there are nodes in the tree, search the key
        curr = self.root
        while curr:
            # key is larger -> search right sub tree
            if key > curr.key:
                curr = curr.right
            # key is smaller -> search left sub tree
            elif key < curr.key:
                curr = curr.left
            # key is found
            else:
                return curr.val
        return -1
    
    def getMin(self) -> int:
        # if there is nothing in root node, return -1
        if not self.root:
            return -1
        
        # if there are nodes in the tree, find the leftmost leaf node
        # since a node should have a value that is bigger than those of nodes in the left sub tree
        curr = self.findMinHelper(node=self.root)
        return curr.val
    
    def findMinHelper(self, node: TreeNode) -> TreeNode:
        # find the leftmost leaf node
        while node and node.left:
            node = node.left
        return node
    
    def getMax(self) -> int:
        # if there is nothing in root node, return -1
        if not self.root:
            return -1
        
        # if there are nodes in the tree, find the rightmost leaf node
        # since a node should have a value that is smaller than those of nodes in the right sub tree
        curr = self.root
        while curr and curr.right:
            curr = curr.right
        return curr.val
    
    def remove(self, key: int) -> None:
        # if there is nothing in root node, nothing to remove
        if not self.root:
            return
        
        # if there are nodes in the tree already, run helper function
        self. root = self.removeHelper(node=self.root, key=key)
        return
        
    def removeHelper(self, node: TreeNode, key: int) -> TreeNode:
        # if there is nothing in node, return None
        if not node:
            return None
        
        # if the target key is larger -> run function on the right sub tree
        if key > node.key:
            node.right = self.removeHelper(node.right, key)
        # if the target key is smaller -> run function on the left sub tree
        elif key < node.key:
            node.left = self.removeHelper(node.left, key)
        # the target key is found, run case 1 or 2 based on the number of children
        else:
            # case 1: 0 or 1 children
            # if left sub tree is empty, replace the node with the right sub tree
            if not node.left:
                return node.right
            # if right sub tree is empty, replace the node with the left sub tree
            elif not node.right:
                return node.left
            # case 2: 2 children
            # find the min node in the right sub tree and replace the node with the min node
            # remove the original min node
            else:
                minNode = self.findMinHelper(node.right)
                node.key = minNode.key
                node.val = minNode.val
                node.right = self.removeHelper(node.right, minNode.key)
        return node
    
    def getInorderKeys(self) -> list[int]:
        result = []
        self.inorderTraversal(self.root, result)
        return result
        
    def inorderTraversal(self, node: TreeNode, result: list[int]) -> None:
        # if there is nothing in the tree, return None
        if not node:
            return
        
        # if there is something in the tree, perform inorder depth-first search
        self.inorderTraversal(node.left, result)
        result.append(node.key)
        self.inorderTraversal(node.right, result)
        return
    
tree = TreeMap()
tree.insert(1, 2)
tree.insert(4, 0)