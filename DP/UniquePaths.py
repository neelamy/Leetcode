# Source : https://leetcode.com/problems/unique-paths/description/

# Algo/DS : DP

# Complexity : O(n^2)


class Solution(object):
   
    
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        dp = [[1 for j in xrange(n)] for i in xrange(m)]      
        for i in xrange(1, m):
            for j in xrange(1, n):
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
        