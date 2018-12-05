# Source : https://leetcode.com/problems/diagonal-traverse/description/

# Algo/DS : Matrix traversal

# Complexity : O(n*m)

# Solution : https://leetcode.com/problems/diagonal-traverse/discuss/97712/Concise-Java-Solution

class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix ==[] : return []
        n = len(matrix) -1
        
        m = len(matrix[0]) -1
        
        
        res = []
        direction = [[-1,1],[1,-1]]
        d= 0
        row, col = 0,0
        for i in range((n+1) * (m+1)):
            #print row, col
            res.append(matrix[row][col])
            row += direction[d][0]
            col += direction[d][1]
            
            '''
            If out of bottom border (row >= m) then row = m - 1; col += 2; change walk direction.
            if out of right border (col >= n) then col = n - 1; row += 2; change walk direction.
            if out of top border (row < 0) then row = 0; change walk direction.
            if out of left border (col < 0) then col = 0; change walk direction.
            Otherwise, just go along with the current direction.
            '''
            if row> n: 
                row = n
                col += 2 # since we are moving to previous row, col+1 is alredy covered so move to col+2
                d = 1-d
            if col> m: 
                col = m
                row += 2
                d = 1-d
            if row < 0: # col is in range so change only row
                row =0
                d = 1-d
            if col< 0: # row is in range so change only row
                col = 0
                d = 1-d
        return res
        