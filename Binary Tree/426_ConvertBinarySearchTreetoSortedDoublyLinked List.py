# Source :https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/description/

# Algo/DS : Tree, circular linked list, inorder traversal

# Complexity : O(n)

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root : return None
        prev, first = None, None
        
        stack = []

        # run till stack or root. Both condition required beacuse initailly root will be empty
        # then perform inorder traversal
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()               
            if not first: first = root
            if not prev : prev = root
            else:
                prev.right = root
                root.left = prev
                prev = root             
            if root.right:
                root = root.right
            else:
                root = None
        first.left = prev
        prev.right = first
        
        return first
       
        
        
  