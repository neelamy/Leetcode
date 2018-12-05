# Source : https://leetcode.com/problems/number-of-islands/description/

# Algo/DS : Graph, DFS

# Complexity : O(n*n)

class Solution(object):

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def issafe(i,j, grid):
            return (0 <= i < len(grid) and 0 <=j < len(grid[0]) and grid[i][j] == "1"  )
        
        def dfs(i,j, grid):    
            grid[i][j] = "0"
            r =[-1,0,0,1]
            c = [0,-1,1,0]
            for i1, j1 in zip(r,c):
                if issafe(i+ i1, j + j1, grid):
                    dfs(i+ i1, j + j1,grid)

        row = len(grid)
        if row <= 0 : return 0
        col = len(grid[0])
        count = 0           
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    dfs(i,j,grid)
                    count += 1       
        return count
    