# Source : https://leetcode.com/problems/diameter-of-binary-tree/description/

# Algo/DS : Binary Tree

# Complexity : O(n), space = O(1)


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def __init__(self):
        self.diameter = 0
        
    def get_height(self, root):
        if not root : return 0
        
        left_height =  self.get_height(root.left)
        right_height = self.get_height(root.right)       
        self.diameter = max(self.diameter, left_height + right_height )
        return 1 + max(right_height, left_height)
    
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.get_height(root)
        return self.diameter