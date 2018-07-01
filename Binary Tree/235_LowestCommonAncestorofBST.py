# Source : https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/

# Algo/DS : Binary Search Tree

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
        
        if not root: return None
        if p.val < root.val and q.val < root.val : return (self. lowestCommonAncestor(root.left, p, q))
        if p.val > root.val and q.val > root.val : return(self. lowestCommonAncestor(root.right, p, q))
        return root
        