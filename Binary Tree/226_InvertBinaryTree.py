# Source : https://leetcode.com/problems/invert-binary-tree/description/

# Algo/DS : Binary Tree

# Complexity : O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.invert(root)
        return root
    
    def invert(self, root):
        
        if not root: return 
        root.left,root.right = root.right, root.left
        self.invert(root.left)
        self.invert(root.right)