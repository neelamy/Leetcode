# Source : https://leetcode.com/problems/binary-tree-preorder-traversal/description/

# Algo/DS : Binary Tree

# Complexity : O(n), space = O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
       
        if not root : return []
        traversal = []
        traversal.append(root.val)
        left_child = self.preorderTraversal(root.left)
        if left_child :traversal.extend(left_child)
        right_child = self.preorderTraversal(root.right)
        if right_child :traversal.extend(right_child)
        return traversal
        
        
        