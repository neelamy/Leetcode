# Source : https://leetcode.com/problems/flood-fill/description/

# Algo/DS : Array

# Complexity : O(n*n)

class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        if image[sr][sc] == newColor: return image
        self.dfs(image, sr,sc,newColor, image[sr][sc])
        return image
        
    def dfs(self,image, i,j,newColor, oldColor):
        image[i][j] = newColor
        if i > 0 and image[i-1][j] == oldColor: self.dfs(image, i-1,j,newColor, oldColor) 
        if j > 0 and image[i][j-1] == oldColor: self.dfs(image, i,j-1,newColor, oldColor)
        if i < len(image) - 1 and image[i+1][j] == oldColor: self.dfs(image, i+1,j,newColor, oldColor) 
        if j< len(image[0]) - 1 and image[i][j+1] == oldColor: self.dfs(image, i,j+1,newColor, oldColor)
        
        
        