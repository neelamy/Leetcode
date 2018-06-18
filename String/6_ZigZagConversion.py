# Source : https://leetcode.com/problems/zigzag-conversion/description/

# Algo/DS : String

# Complexity : O(1)

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1: return s
        
        ans =[""] * numRows
        
        add = True
        
        position = 0
        
        for char in s:
            ans[position] = ans[position] + char        
            if position == 0: add = True
            if position == numRows -1: add = False      
            if add == True : position += 1
            else: position -= 1
                
        return "".join(ans)