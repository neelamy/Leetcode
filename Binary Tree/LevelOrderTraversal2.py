
# Source : https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/

# Algo/DS : Binary Tree

# Complexity : O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def bfs(self, root):     
        if root is None: return []
        
        queue = [[0, root]]
    
        l = 0
        ans = []; t = []
        while queue:        
            temp =  queue.pop(0)  
            level = temp[0]
            node = temp[1]
           
            if l == level:
                t.append(node.val)
            else:
                
                ans.append(t)
                t = []
                l = level
                t.append(node.val)
            if node.left is not None : queue.append([level+1, node.left])
            if node.right is not None : queue.append([level+1, node.right])
            
        ans.append(t)        
        return ans[::-1]
                
               
                
     
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        return self.bfs(root)
