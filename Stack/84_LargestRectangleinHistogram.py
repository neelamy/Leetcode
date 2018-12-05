# Source : https://leetcode.com/problems/largest-rectangle-in-histogram/description/

# Algo/DS : Histogram, stack

# Complexity : O(n)


class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights: return 0
        stack = []
        max_area = 0
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                bar = stack.pop()
                RHS = i
                LHS = stack[-1] if stack else 0
                if not stack:
                    max_area = max(max_area, (RHS *heights[bar]))
                else:
                    max_area = max(max_area, (RHS - LHS -1 )*heights[bar])
            stack.append(i)
        
               
        while stack:
            bar = stack.pop()
            RHS = i + 1
            LHS = stack[-1] if stack else 0
            if not stack:
                max_area = max(max_area, RHS *heights[bar])
            else:
                max_area = max(max_area, (RHS - LHS -1 )*heights[bar])
                
        return max_area
