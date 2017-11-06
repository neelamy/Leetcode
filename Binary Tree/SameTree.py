# Source : https://leetcode.com/problems/same-tree/description/
# Given two binary trees, write a function to check if they are the same or not.

# Algo/DS : Binary Tree

# Complexity : O(n)




# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



class Solution(object):
       
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is not None : return False
        if q is None and p is not None : return False
        if q is None or p is  None : return True
        if p.val != q.val : return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            
