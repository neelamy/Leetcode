# Source : https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/

# Algo/DS : Binary Tree

# Complexity : O(log n), space = O(1)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        if root in [None, p, q] : return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # if left and right then that means one value is in right and one in left
        # so return root
        if left and right : return root

        #return the value which isnt none as values are on that side
        return left or right
        