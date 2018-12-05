# Source : https://leetcode.com/problems/recover-binary-search-tree/description/

# Algo/DS : Tree

# Complexity : O(n)

'''
We need to find the first and second elements that are not in order right?

How do we find these two elements? For example, we have the following tree that is printed as in order traversal:

6, 3, 4, 5, 2

We compare each node with its next one and we can find out that 6 is the first element to swap because 6 > 3 and 2 is the second element to swap because 2 < 5.

Really, what we are comparing is the current node and its previous node in the "in order traversal".
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.first = None
        self.second = None
        self.prev = TreeNode(-float("Inf"))
        self.traverse(root)
        self.first.val ,self.second.val = self.second.val ,self.first.val

        
    def traverse(self, root):
        if not root: return
        self.traverse(root.left)
        
        if not self.first and self.prev.val > root.val:
            self.first = self.prev
            
        if self.first and self.prev.val > root.val:
            self.second = root
        
        self.prev = root
        self.traverse(root.right)
        
                
        