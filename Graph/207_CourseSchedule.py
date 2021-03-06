
# Source : https://leetcode.com/problems/course-schedule/description/

# Algo/DS : Graph, Topological sort

# Complexity : O(V+E)

from collections import defaultdict
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if len(prerequisites) == 0: return True

        d = defaultdict(list)
        degree = defaultdict(int)

        # create graph and store degree
        for u, v in prerequisites:
            d[u] = d.get(u, []) + [v]
            degree[v] = degree.get(v, 0) + 1
            
        stack, res = [], []
        #store ALL nodes with degree 0
        # all nodes are required because somtimes many courses may not have dependency
        # so they will never be in final res
        for v in range(numCourses):
            if degree[v] == 0: 
                stack.append(v)

        # perform topological sort
        while stack:           
            n = stack.pop(0)

            # append node to result
            res.append(n)

            # get its neighbours
            for v in d[n]:
                # reduce their degree. if degree = 0 then add to stack
                degree[v] -=1
                if degree[v] == 0: stack.append(v)
        
        # return True if all courses are there in result    
        return len(res) == numCourses
            
            
        
        