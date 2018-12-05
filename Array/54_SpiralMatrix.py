
# Source : https://leetcode.com/problems/spiral-matrix/description/

# Algo/DS : Array

# Complexity : O(n*n)


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        result = []
              
        if matrix == [] : return result
        row_max = len(matrix) -1
        col_max = len(matrix[0]) - 1  

        col_min , row_min= 0, 0
 
        while row_min <= row_max and col_min <= col_max:


            for col in range(col_min, col_max + 1):
                result.append(matrix[row_min][col])

            row_min += 1
            
            for row in range(row_min, row_max + 1):
                result.append(matrix[row][col_max])

            col_max -= 1

            # move only if row left
            if row_min <= row_max  : 
                for col in range(col_max , col_min - 1 , -1):
                    result.append(matrix[row_max][col])
            row_max -= 1
            
            # move only if col left
            if col_min <= col_max:
                for row in range(row_max, row_min -1 , -1):
                    result.append(matrix[row][col_min])

            col_min += 1
            
        return result
        