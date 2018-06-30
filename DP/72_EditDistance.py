# Source : https://leetcode.com/problems/edit-distance/description/

# Algo/DS : DP

# Complexity : O(n ^ 2)

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n = len(word1)
        m = len(word2)
        dp =[[0 for j in range(m + 1)] for i in range(n + 1)]       
        dp[0] = [i for i in range(m + 1)]   
        for i in range(n + 1):
            dp[i][0] = i
        for i in range(1,n+1):
            for j in range(1, m+1):
                if word1[i-1] == word2[j-1] : 
                    dp[i][j] = dp[i-1][j-1] 
                else:
                	# insert, delete, replace
                    dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
                    
        return dp[-1][-1]
