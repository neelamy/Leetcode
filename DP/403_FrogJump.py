# Source : https://leetcode.com/problems/frog-jump/description/

# Algo/DS : Set, DP

# Complexity : O(n*2)

# explanation : https://leetcode.com/problems/frog-jump/solution/


class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        jump = {}
        
        # USE set as LIST gives TLE
        for i in stones:
            jump[i] = set()
            
        jump[0].add(0)
       
        for i in stones:
            for k in jump[i]:
                for step in [k-1, k, k+1]:
                    # i+ step != i else error that set size is changed during iteration
                    if i+ step != i and i+ step in jump:
                        jump[i+ step].add(step)
                        
        return len(jump[stones[-1]]) != 0
      