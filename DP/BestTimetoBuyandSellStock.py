# Source : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

# Algo/DS : DP

# Complexity : O(n)

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        high = 0; max_profit = 0       
        for p in prices[::-1]:         
            high = max(p , high)                   
            max_profit = max(max_profit, high - p)           
        return max_profit