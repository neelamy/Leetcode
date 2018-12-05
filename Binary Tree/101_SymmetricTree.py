# Source : https://leetcode.com/problems/symmetric-tree/description/

# Algo/DS : Binary Tree

# Complexity : O(n log n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# https://leetcode.com/problems/symmetric-tree/discuss/33054/Recursive-and-non-recursive-solutions-in-Java

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        return self.check(root.left, root.right)
        
        
    def check(self, p, q):      
        if not p and not q : return True
        if not p or not q : return False        
        if p.val != q.val : return False
        return self.check(p.left, q.right) and self.check(p.right, q.left)
        