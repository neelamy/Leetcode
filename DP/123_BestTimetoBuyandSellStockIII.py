
# Source : https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/

# Algo/DS : Array, stock, DP

# Complexity : O(n)

# CHECK : https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/discuss/108870/Most-consistent-ways-of-dealing-with-the-series-of-stock-problems


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0
        
        # forward traversal, profits record the max profit 
        # by the ith day, this is the first transaction
        # we buy at i
        mini = prices[0]
        max_profit = 0
        profit = []
        
        for i in range(len(prices)):
            mini = min(mini, prices[i])
            max_profit = max(max_profit,prices[i] - mini )
            profit.append(max_profit)
            
            
        maxi = prices[-1]
        max_profit = 0
        
        # backward traversal, max_profit records the max profit
        # after the ith day, this is the second transaction 
        # we sell at i
        for i in range(len(prices)-1, -1, -1):
            maxi = max(maxi, prices[i])
            max_profit = max(max_profit, maxi - prices[i] )
            profit[i] += max_profit
            
        return max(profit)
            
            
        
        
        
        