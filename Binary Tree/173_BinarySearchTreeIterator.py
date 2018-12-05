
# Source : https://leetcode.com/problems/binary-search-tree-iterator/description/

# Algo/DS : BST, tree

# Complexity : O(1) for has next, Average - O(1)/ worst -O(n) for next

# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []      
        self.fill_stack(root)
    
    # append left branch in stack
    def fill_stack(self, root):       
        while root:
            self.stack.append(root)
            root = root.left
        
    # next exist only if stack has any element
    def hasNext(self):
        """
        :rtype: bool
        """
        return self.stack
        
    
    # smallest number will be leaf of left most branch so at the top of stack
    # once that is popped, insert its right child in stack
    def next(self):
        """
        :rtype: int
        """
        node = self.stack.pop()
        self.fill_stack(node.right)
        return node.val
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())