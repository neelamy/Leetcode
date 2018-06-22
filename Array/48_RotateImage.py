# Source : https://leetcode.com/problems/rotate-image/description/

# Algo/DS : Array

# Complexity : O(n^2)

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        #transpose the matrix
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
        # reverse the matrix
        for i in range(n):
            for j in range(n/2):
                matrix[i][j], matrix[i][n - 1 - j] = matrix[i][n - 1 - j], matrix[i][j]
                

# Alternate solution: matrix[:] = [[row[i] for row in reversed(matrix)] for i in range(len(matrix))]
                
