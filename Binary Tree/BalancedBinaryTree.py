# Source : https://leetcode.com/problems/balanced-binary-tree/description/

# Algo/DS : Binary Tree

# Complexity : O(n log n)


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def get_height(self, n):
        if n == None: return 0
        lheight = self.get_height(n.left)
        if lheight == -1 : return -1
        rheight = self.get_height(n.right)
        if rheight == -1 : return -1
        if abs(lheight - rheight) >1 : return -1
        return 1 + max( lheight , rheight)
    
    
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.get_height(root) != -1 