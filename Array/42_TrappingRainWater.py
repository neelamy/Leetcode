# Source : https://leetcode.com/problems/trapping-rain-water/description/

# Algo/DS : Array 

# Complexity : O(n), space = O(1)

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        n = len(height)
        LHS = height[:]
        RHS = height[:]
        
        for i in range(1, n):
            LHS[i] = max(LHS[i-1], LHS[i])
            
        for i in range(n-2, -1, -1):
            RHS[i] = max(RHS[i+1], RHS[i])
            
        water_contained = [min(LHS[i], RHS[i]) - height[i] for i in range(n)]
        return sum(water_contained)
        