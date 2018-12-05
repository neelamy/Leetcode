# Source : https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

# Algo/DS : Binary Tree

# Complexity : O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        reverse = False
        stack = []
        if root: stack.append(root)       
        while stack:           
            val = [node.val for node in stack] 
            if reverse : val = val[::-1]
            result.append(val)
            reverse = not reverse
            stack = [kid for node in stack for kid in [node.left, node.right] if kid ]
        return result
        