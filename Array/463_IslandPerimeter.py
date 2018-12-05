# Source : https://leetcode.com/problems/island-perimeter/description/

# Algo/DS : Array

# Complexity : O(n^2)

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        row = len(grid) 
        col = len(grid[0])
        
        count = 0
       
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    temp = 0
                    if i > 0 and grid[i - 1][j] == 1 : temp += 1
                    if j > 0 and grid[i][j - 1] == 1 : temp += 1
                    if i < row-1 and grid[i + 1][j] == 1 : temp += 1
                    if j < col-1 and grid[i ][j + 1] == 1 : temp += 1
                    count += 4 - temp
        return count
              
    