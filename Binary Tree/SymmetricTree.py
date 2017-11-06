# Source : https://leetcode.com/problems/symmetric-tree/description/
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

# Algo/DS : Binary Tree

# Complexity : O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    
    
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        
        """
        
        q =[]
        q.append(root)
         
        while q:     
            s = []
            temp =  []
            while q:
                node = q.pop(0)
                s .append(node.val) if node is not None else s.append(-1)
                if node is not None: temp.append(node.left)     
                if node is not None: temp.append(node.right)              
            q = temp  
            i = 0 ; j = len(s) -1         
            while i<j:          
                if s[i] != s[j] : return False
                i += 1
                j -=1
                
        return True