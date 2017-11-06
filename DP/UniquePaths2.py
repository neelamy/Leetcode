# Source : https://leetcode.com/problems/unique-paths-ii/description/

# Algo/DS : DP

# Complexity : O(n^2)


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for j in xrange(n)] for i in xrange(m)]  
        
        for i in xrange( m):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = 1 
            else: break
                 
        for i in xrange( n):
            if obstacleGrid[0][i] == 0:
                dp[0][i] = 1 
            else: break
         
        for i in xrange(1, m):
            for j in xrange(1, n): 
                    if obstacleGrid[i][j] != 1 :
                        dp[i][j] = dp[i-1][j] + dp[i][j-1]
       
         
        return dp[-1][-1]