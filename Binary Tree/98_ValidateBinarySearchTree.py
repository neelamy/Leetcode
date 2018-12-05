 def __init__(self):
        self.predecessor = None     
        
    def isValidBST(self, root):
        return self.isValid(root)
    
    def isValid(self, root):
        if root is None:
            return True
        if not self.isValid(root.left):
            return False
        if self.predecessor and self.predecessor.val >= root.val:
            return False
        self.predecessor = root
        return self.isValid(root.right)