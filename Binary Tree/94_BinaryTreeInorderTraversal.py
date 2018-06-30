# Source : https://leetcode.com/problems/binary-tree-inorder-traversal/description/

# Algo/DS : Binary Tree

# Complexity : O(n), space = O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def __init__(self):
        self.traversal = []
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        if root:
            self.inorderTraversal(root.left)
            self.traversal.append(root.val)
            self.inorderTraversal(root.right)           
            
        return self.traversal
        
        
        