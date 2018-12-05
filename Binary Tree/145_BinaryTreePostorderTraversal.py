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



# using stack

class Solution(object):
        
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        traversal,queue = [],[]
        if not root : return traversal
        while True:          
            while(root):
                if root.right is not None: queue.append(root.right)
                queue.append(root)
                root = root.left
               
            root = queue.pop()
            
            if queue and root.right and root.right.val == queue[-1].val:
                queue.pop()
                queue.append(root)
                root = root.right
            else:
                traversal.append(root.val)
                root = None
            if not queue: break
        return traversal
            
               