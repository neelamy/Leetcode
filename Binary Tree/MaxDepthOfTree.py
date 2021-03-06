# Source : https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
# Maximum Depth of Binary Tree.

# Algo/DS : Binary Tree

# Complexity : O(n)


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """      
        return 0 if root is None else 1 + max(self.maxDepth(root.left),self.maxDepth(root.right) )