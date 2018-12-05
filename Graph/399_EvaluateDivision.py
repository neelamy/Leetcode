# Source : https://leetcode.com/problems/evaluate-division/description/

# Algo/DS : Graph, DFS

# Complexity : O(V+E)

from collections import defaultdict
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """

        # Create Graph
        self.graph = self.createGraph(equations, values)
        res = []

        # iterate queries
        for q in queries:
            u,v  = q[0], q[1]

            # if any node is not present then ans = -1
            if u not in self.graph or v not in self.graph: ans = -1.0
            else:
                # else find and
                ans = self.solve(u,v,set(), 1.0)
            if ans == None: ans = -1.0  
            res.append(ans)
        return res
        
    # add edges in both directions
    def createGraph(self,equations, values):
        graph = defaultdict(dict)       
        for i in range(len(equations)):
            u , v = equations[i][0], equations[i][1]
            graph[u][v] = values[i]
            graph[v][u] = 1.0/values[i]
        return graph
    
    # traverse graph to get answer
    # visited is a set
    # val is passed with values found so far
    def solve(self, u, v, visited,val):       
        if u == v : return val
        for next in self.graph[u]:
            if next not in visited:
                visited.add(next)
                output =  self.solve(next, v, visited,val* self.graph[u][next]) 
                if output != None: return output
                
        return None
        
        