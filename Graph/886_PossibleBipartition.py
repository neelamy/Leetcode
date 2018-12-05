# Source : https://leetcode.com/problems/possible-bipartition/description/

# Algo/DS : Graph, BFS, Bipartite

# Complexity : O(V+E)

class Solution(object):
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        
        d = {}
        
        # we need to add undirectional edges so that if 2--> 42 and we reach 42 by
        # some other node then we should be able to color 2 with opposite color 
        for u , v in dislikes:
            d[u] = d.get(u,[]) + [v]
            d[v] = d.get(v,[]) + [u]
        
        # use color instead of visited to avoid TLE
        color = [0] * (N+ 1)     
        for i in range(1, N+1):
            if color[i] != 0 or i not in d: continue         
            color[i] = 1            
            queue =[i]
            while queue:
                node = queue.pop(0)
                if node not in d: continue
                for v in d[node]:
                    if color[v] == color[node]: 
                        return False
                    if color[v] ==0:
                        color[v] = -color[node]
                        queue.append(v)
                    
                    
        return True

                
                
                
                