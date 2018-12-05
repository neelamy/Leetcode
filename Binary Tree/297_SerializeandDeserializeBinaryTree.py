# Source : https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/

# Algo/DS : Tree

# Complexity : O(n)


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        return self.preorder( root)
    
        
    def preorder(self, root):
        if not root: return ["None"]
        result = []
        result.append(root.val)
        result += self.preorder(root.left)
        result +=self.preorder(root.right)
        return result
  

    def deserialize(self, data):
        """Decodes your encoded data to tree.      
        :type data: str
        :rtype: TreeNode
        """
        self.index = 0
        return self.createtree(data)
        
    def createtree(self, preorder):       
        if self.index == len(preorder): return None
        if preorder[self.index] == "None":
            self.index += 1
            return None        
        root = TreeNode(preorder[self.index])
        self.index += 1       
        root.left= self.createtree(preorder)
        root.right =self.createtree(preorder)
        return root 
            
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))