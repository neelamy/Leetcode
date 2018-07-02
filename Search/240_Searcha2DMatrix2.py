# Source : https://leetcode.com/problems/search-a-2d-matrix-ii/description/

# Algo/DS : Matrix

# Complexity : O(n^2)

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if  len(matrix)<= 0: return False
        
        max_col = len(matrix[0]) -1 
        max_row = len(matrix) -1 
        i , j = 0, max_col
        while i <= max_row and  j >=0:
            if matrix[i][j] == target : return True
            elif matrix[i][j] > target: j -= 1
            else: i += 1           
        return False
        