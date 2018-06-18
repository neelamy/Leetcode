class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height) - 1
        m = 0
        while(l < r):
            width = r - l
            current_water = min(height[l], height[r]) * width
          
            m = max(m, current_water)
            
            if height[l] >= height[r]:
                r -= 1
            else:
                l +=1
        return m
            
                
        