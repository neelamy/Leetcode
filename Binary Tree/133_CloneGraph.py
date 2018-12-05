# Source : https://leetcode.com/problems/clone-graph/description/

# Algo/DS : Binary Tree

# Complexity : O(n)

# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:

    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):      
        #if not node : return node
        self.d  = {}
        return self.clone(node)
        
    def clone(self, node): 
        if not node : return

        # if its in d then it has been cloned so return its copy
        if node in self.d : return self.d[node]

        # else create its copy
        new_node = UndirectedGraphNode(node.label)

        # add it in d so that its not cloned again
        self.d[node] = new_node

        # clone and copy its neighbor and append them to neighbour list
        for neighbour in node.neighbors:
            new_node.neighbors.append(self.clone(neighbour))

        # return cloned node
        return new_node
       
        
        