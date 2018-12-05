# Source : https://leetcode.com/problems/is-graph-bipartite/description/

# Algo/DS : Graph, BFS, Bipartite

# Complexity : O(V+E)

class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
       
        # set initial color for all to 0
        color = [0] * len(graph)
        visited =[False] * len(graph)
        
        # for loop is needed so that all disconnect nodes can be covered
        for i in range(len(graph)):

            # if already visited or no neighbor then skip this node
            if visited[i] or len(graph[i]) == 0: continue
            
            # set color to 1 and start BFS
            color[i] = 1
            queue = [i]
            while queue:
                node = queue.pop(0)
                visited[node] = True                
                for neigh in graph[node]:
                    if color[neigh] == color[node]: return False

                    # if neighbour is not visited then set color and add to queue
                    if not visited[neigh]:                   
                        color[neigh] = -color[node]
                        queue.append(neigh)
      
        return True