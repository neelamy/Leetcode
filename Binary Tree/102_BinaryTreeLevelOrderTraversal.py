# Source : https://leetcode.com/problems/binary-tree-level-order-traversal/description/

# Algo/DS : Tree

# Complexity : O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.result = []
        
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None : return  []
        stack = []        
        stack.append(root)
        while stack:
            level = [node.val for node in stack if node]
            self.result.append(level)
            stack = [kid for node in stack for kid in [node.left, node.right] if kid]
        return self.result