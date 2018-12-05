# Source : https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/

# Algo/DS : Array, DP

# Complexity : O(log n)

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0        
        for index in range(1, len(prices)):
            max_profit += max(0,prices[index] - prices[index -1])
        return max_profit