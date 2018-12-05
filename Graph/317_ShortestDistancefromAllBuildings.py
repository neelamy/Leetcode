# Source : https://leetcode.com/problems/shortest-distance-from-all-buildings/description/

# Algo/DS : BFS, graph

# Complexity : O(number of 1)O(number of 0) ~ O(m^2n^2)

class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        # this will store total dist from all houses
        self.dist = [[[0,0] for j in range(len(grid[0]))] for i in range(len(grid))]

        # to keep track of total houses
        total_house = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):

                # if house found, start bfs
                if grid[i][j] == 1:
                    total_house += 1
                    self.bfs(grid, i, j)
        
        
      
        least_dist = float("Inf")
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                distance, house_covered = self.dist[i][j]

                # check if grid was zero and all houses can be reached
                if house_covered == total_house and grid[i][j] == 0 :
                    least_dist = min(least_dist, distance)
                
                       
        return least_dist if least_dist != float("Inf") else -1
                    
        
        
    # perform bfs  
    def bfs(self, grid, i1,j1):
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        queue = []
        queue.append([i1,j1, 0])
        while queue:   
            i, j, count = queue.pop(0)
            visited[i][j] = True
            self.dist[i][j][0] += count
            self.dist[i][j][1] += 1
            if i > 0 and grid[i-1][j] == 0 and not visited[i-1][j]:
                queue.append([i-1,j, count + 1])
                visited[i-1][j] = True
            if j > 0 and grid[i][j-1] == 0 and not visited[i][j-1]:
                queue.append([i,j-1, count + 1])
                visited[i][j-1] = True
            if i < len(grid)-1 and grid[i+1][j] == 0 and not visited[i+1][j]:
                queue.append([i+1,j, count + 1])
                visited[i+1][j] = True
            if j < len(grid[0])-1 and grid[i][j+1] == 0 and not visited[i][j+1]:
                queue.append([i,j+1, count + 1])
                visited[i][j+1] = True
                
        
     