# Source : https://leetcode.com/problems/closest-binary-search-tree-value/description/

# Algo/DS : Binary Tree

# Complexity : O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        self.diff = float("Inf")
        self.res = None
        self.find(root,target)
        return self.res
        
        
    def find(self, root, target):
        if not root: return
        
        diff = abs(root.val - target)
        #print 
        if diff < self.diff:
            self.diff= diff
            self.res = root.val
        
        if root.val > target:
            self.find(root.left,target)
        else:
            self.find(root.right,target)
        
       
        