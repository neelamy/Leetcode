# Source : hhttps://leetcode.com/problems/binary-tree-vertical-order-traversal/description/

# Algo/DS : Tree

# Complexity : O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
        
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None: return []
        order = {}
        stack = [(root, 0)]
        # we do BFS so that we can get nodes in top down manner and from left to right
        while stack:
            node , level = stack.pop(0)
            if node is None : continue
            order[level] = order.get(level, []) + [node.val]
            stack.append((node.left, level - 1))
            stack.append((node.right, level + 1))
        return [order[v] for v in sorted(order)]
