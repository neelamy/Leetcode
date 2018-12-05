# Source : https://leetcode.com/problems/coin-change-2/description/

# Algo/DS : DP, coin change

# Complexity : O(nm) n = number of coin m = amount

class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        n = len(coins) 
        dp = [[0 for j in range(amount + 1)] for i in range(n + 1)]
        
        for i in range(n+1):
            dp[i][0] = 1
            
        for i in range(1, n+1):
            for j in range(1, amount + 1):
                if coins[i-1] > j:dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i-1]]
        return dp[-1][-1]
            
        
        