# Source : https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/

# Algo/DS : Binary Tree, linked list

# Complexity : O(n), space = O(1)


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#https://leetcode.com/problems/flatten-binary-tree-to-linked-list/discuss/157485/Simple-Python-Stack-Solution

class Solution(object):
    def __init__(self):
        self.prev = None
        
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root is None : return root
      
        self.flatten(root.right)
        self.flatten(root.left)
        root.right = self.prev
        root.left = None
        self.prev = root
        
        
        