# Source : https://leetcode.com/problems/binary-tree-postorder-traversal/description/

# Algo/DS : Binary Tree

# Complexity : O(n), space = O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def __init__(self):
        self.traversal = []
        
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root:
            self.postorderTraversal(root.left)
            self.postorderTraversal(root.right)           
            self.traversal.append(root.val)
        return self.traversal
            
               